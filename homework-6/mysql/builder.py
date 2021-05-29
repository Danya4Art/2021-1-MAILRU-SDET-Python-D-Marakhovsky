from mysql.models import Lenght, Types, Count, Val, Error

class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_string(self, key, info):
        
        string = None

        if key == 'lenght':
            string = Lenght(num=info['num'])
        elif key == 'types':
            string = Types(req=info['req'], count=info['count'])
        elif key == 'count':
            string = Count(count=info['count'], url=info['url'])
        elif key == 'val':
            string = Val(
                        url = info['url'],
                        code = info['code'],
                        val = info['val'],
                        ip =  info['ip']
                        )
        elif key == 'error':
            string = Error(ip=info['ip'], count=info['count'])
        else:
            return
            
        self.client.session.add(string)
        return string
