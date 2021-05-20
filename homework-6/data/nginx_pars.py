import re

nginx_pattern = re.compile(r"(?P<ip>([\d]+)\.([\d]+)\.([\d]+)\.([\d]+))"
    r"\s-\s-\s(?P<date>\[.+\])\s\"(?P<req>.+)\s(?P<url>.+)\s(HTTP/1\.\d)\"\s"
    r"(?P<code>\d+)\s(?P<value>\d*)")

def req_num(log):
    return [{'num': str(len(log))}]

def req_typ(log):
    res = []
    for line in log:
        answer = nginx_pattern.search(line)
        if answer:
            res += [answer.group("req")]
    res = [(x, res.count(x)) for x in set(res)]
    res.sort(key = lambda x: x[1], reverse = True)
    return [{'req': res[i][0], 'count': res[i][1]} for i in range(len(res))]

def req_cnt(log):
    res = []
    for line in log:
        answer = nginx_pattern.search(line)
        if answer:
            res += [answer.group("url")]
    res = [(res.count(x), x) for x in set(res)]
    res.sort(key = lambda x: x[0], reverse = True)
    return [{'count': res[i][0], 'url': res[i][1]} for i in range(min(10,len(res)))]

def req_val(log):
    res = []
    for line in log:
        answer = nginx_pattern.search(line)
        if answer and re.match(r"4\d{2}", answer.group("code")):
            res += [(answer.group("url"), 
                answer.group("code"), 
                int(answer.group("value")), 
                answer.group("ip"))]
    res.sort(key = lambda x: x[2], reverse = True)
    return  [
                {
                'url': res[i][0],
                'code': res[i][1],
                'val': res[i][2],
                'ip': res[i][3]
                }
            for i in range(min(5,len(res)))
            ]

def user_err(log):
    res = []
    for line in log:
        answer = nginx_pattern.search(line)
        if answer and re.match(r"5\d{2}", answer.group("code")):
            res += [answer.group("ip")]
    res = [(x, res.count(x)) for x in set(res)]
    res.sort(key = lambda x: x[1], reverse = True)
    return [{'ip': res[i][0], 'count': res[i][1]} for i in range(min(5,len(res)))]

def make_data(key, log_file):

    log = open(log_file, 'r').readlines()

    data = {
    'lenght': req_num,
    'types': req_typ,
    'count': req_cnt,
    'val': req_val,
    'error': user_err
    }

    value = data[key](log)
    return value
