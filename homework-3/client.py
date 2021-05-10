import requests
import pytest
import requests
import re
import json
import datetime
import random
from time import sleep
from _pytest.fixtures import FixtureRequest
from requests.cookies import cookiejar_from_dict


class ApiClient:

    cookies_list = []


    def __init__(self):
        self.session = requests.Session()
        self.csrf_token = None


    def find_cookies(self, all_cookies, cookies_names):
        pattern = r'Cookie (\w+)=(\w+)'
        find_all = re.findall(pattern, str(all_cookies))
        return [{'name': i[0], 'value': i[1]} for i in find_all if i[0] in cookies_names]


    def login(self, user, password):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        headers = {'Referer': 'https://target.my.com/'}
        data = {
        'email': user,
        'password': password,
        'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        }
        result = self.session.post(location, headers=headers, data=data)
        if 'csrf_token' in str(result.headers):
            return None
        self.session.get('https://target.my.com/csrf/')
        self.csrf_token = self.find_cookies(str(self.session.cookies), 'csrftoken')[0]['value']
        cookies_names = ['sdcs', 'mc']
        new_cookies_list = self.find_cookies(self.session.cookies, cookies_names)
        return new_cookies_list


    def create_campaign(self, adress_image, campaign_url):
        location = 'https://target.my.com/api/v2/content/static.json'
        files = {
            'file': open(adress_image, 'rb'),
            "width":240,
            "height":400
        }
        headers = {
        'X-CSRFToken': self.csrf_token
        }
        result = self.session.post(location, headers=headers, files=files)
        image_id = result.json()['id']
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        d = datetime.datetime.now()
        n = d + datetime.timedelta(1)
        payload = {
            "name":f"Новая кампания {d.strftime('%d.%m.%Y %H:%M:%S')}",
            "objective":"traffic",
            "enable_offline_goals":False,
            "targetings":{
                "split_audience":[1,2,3,4,5,6,7,8,9,10],
                "sex":["male","female"],
                "age":{
                    "age_list":[26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60],
                    "expand":True
                },
                "geo":{"regions":[188]},
                "interests_soc_dem":[],
                "segments":[],
                "interests":[],
                "fulltime":{
                    "flags":[
                        "use_holidays_moving",
                        "cross_timezone"
                    ],
                    "mon":[0,1,2,3,4,5],
                    "tue":[0,1,2,3,4,5],
                    "wed":[0,1,2,3,4,5],
                    "thu":[0,1,2,3,4,5],
                    "fri":[0,1,2,3,4,5],
                    "sat":[0,1,2,3,4,5],
                    "sun":[0,1,2,3,4,5]
                },
                "pads":[102643],
                "mobile_types":["tablets","smartphones"],
                "mobile_vendors":[],
                "mobile_operators":[]
            },
            "date_start":f"{d.strftime('%Y-%m-%d')}",
            "date_end":f"{n.strftime('%Y-%m-%d')}",
            "autobidding_mode":"second_price_mean",
            "mixing":"fastest",
            "enable_utm":True,
            "price":"8.04",
            "max_price":"0",
            # Признаюсь, что этот id взят с потолка и не привязан к акку
            "package_id":961,
            "banners":
                [{
                # Этот тоже
                "urls":{"primary":{"id":46978661}},
                "textblocks":{},
                "content":{"image_240x400":{"id":f"{image_id}"}},
                "name":""
            }]
        }
        result = self.session.post('https://target.my.com/api/v2/campaigns.json', headers=headers, data=json.dumps(payload))
        assert '20' in str(result)
        return result.json()['id']


    def delete_campaign(self, campaign_id):
        location = 'https://target.my.com/api/v2/campaigns/mass_action.json'
        payload = [{"id":campaign_id,"status":"deleted"}]
        headers = {
        'X-CSRFToken': self.csrf_token
        }
        result = self.session.post(location, headers=headers, data=payload)
        assert '20' in str(result)


    def create_segment(self):
        location = 'https://target.my.com/api/v2/remarketing/segments.json'
        headers = {
        'X-CSRFToken': self.csrf_token
        }
        d = datetime.datetime.now()
        payload = {
            "name": f"Сегмент {d.strftime('%d.%m.%Y %H:%M:%S')}", 
            "pass_condition": 1,
            "relations": [  
                {  
                  "object_type":"remarketing_player",
                  "params":{
                        "type":"positive", 
                        "left":360, 
                        "right":0
                    }
                },
                {  
                  "object_type":"remarketing_player",
                  "params":{"type":"positive", "left":360, "right":0}
                }
            ]
        }
        result = self.session.post(location, data=json.dumps(payload), headers=headers)
        assert '20' in str(result)


    def delete_segment(self, segemt_id):
        location = 'https://target.my.com/api/v1/remarketing/mass_action/delete.json'
        headers = {
        'X-CSRFToken': self.csrf_token
        }
        payload = [{"source_id":segment_id,"source_type":"segment"}]
        result = self.session.post(location, data=json.dumps(payload), headers=headers)
        assert '20' in str(result)