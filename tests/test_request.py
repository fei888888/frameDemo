import json
from datetime import datetime
import requests
import pytest
class TestRequest:
    #get请求体构造
    def test_get(self):
        payload={
            "name":"lhys.notNeed"
        }
        r=requests.get('http://zj.gcjs.zdvictory.com/unionpro/unionpro/ignorecheck/sysPara/findByName',params=payload)
        print(r.text)
        assert r.status_code==200
    def test_get2(self):
        url='http://zj.gcjs.zdvictory.com/gcjs/ggfw/yygl/approve-reserve-manage!save.action'
        payload={
            "reserveType": 1,
            "reserveBusiness": 1,
            "xzqhdm": 440800,
            "address": 444,
            "telephone": 15836265262,
            "reserveDate":datetime.now()
        }
        headers={
            "Content-Type":"application/json",
            "charset":"UTF-8"}
        r=requests.get(url,params=payload,headers=headers)
        print(r.json())
        assert r.status_code==200
    def test_file(self):
        # post/header/文件上传请求体构造
        url='http://zj.gcjs.zdvictory.com/unionpro/unionpro/v-api/file/upload'
        cookies = {'enwiki_session': '_fbp=fb.1.1631863117597.1100536157; front-sso-data=RnRLTnJlaXB2SHdQdERXa2Rybm5WT0Y3RXNVSkZHTEMwQzdWNVV3MU5Ba3F0WGJZL2l5YnpjZDh0ZytCOWdwNDhLT2VmTnM1N3hGYjJITTJQOUswRWY4dmVoTnV0WkJrbytYV2ZaK2UzSExsc2pTeGpmVWl0Lys1RTFrb0gvcXd0WnN4S1JUWlpqaTRZSG1IZ1hIcVdkWUFGU1p4SjVhbHFUZFRMUFMyc3paODcrc0grWGN3bG5keVQ2Z043cmYrZjRHTGJUbFV2K21aOE4wWnM1cEhlK014UnRRUzFyLzFmSXJXVk9zb0pCS1V0ZnRRL0NNRjdpS2RxcWNLTS9udHpqZDV5NmZwQmEyUTFoR2I0aU9QQkhjOFo0YnR1eXNyVkNzUlFibWNKV0xpSVFCUktSc3I0SmJhQ0RZTk41YXVrbmNGTEMyRFVLc1prSW5RZ2FOcXVKOWtreU1VSkN0TWhrbzIyNVFSeGZ3cm9IQldodTRqRmoxWUtoN2krQVFuL1FmZ1JvMHFrS2ZNNFlUOC9MWmZac1piMXlVaENTRzY0TWdpR0FvS0JsU0ZnekpaQ2VJSTF5V0dWL0RLZk5UTDhhYzd4VzljQmtRUTdoZnNNOFhEYjlQbWJQYi9aTFIzZE9jWDFBc0dQeHUwOXFkUk9VK3ViK1BSYlZmM09ONFk1dkZkMkE4U3hUeExVRDNvdng0YW9RPT0='}
       # cookies=_fbp=fb.1.1631863117597.1100536157; front-sso-data=RnRLTnJlaXB2SHdQdERXa2Rybm5WT0Y3RXNVSkZHTEMwQzdWNVV3MU5Ba3F0WGJZL2l5YnpjZDh0ZytCOWdwNDhLT2VmTnM1N3hGYjJITTJQOUswRWY4dmVoTnV0WkJrbytYV2ZaK2UzSExsc2pTeGpmVWl0Lys1RTFrb0gvcXd0WnN4S1JUWlpqaTRZSG1IZ1hIcVdkWUFGU1p4SjVhbHFUZFRMUFMyc3paODcrc0grWGN3bG5keVQ2Z043cmYrZjRHTGJUbFV2K21aOE4wWnM1cEhlK014UnRRUzFyLzFmSXJXVk9zb0pCS1V0ZnRRL0NNRjdpS2RxcWNLTS9udHpqZDV5NmZwQmEyUTFoR2I0aU9QQkhjOFo0YnR1eXNyVkNzUlFibWNKV0xpSVFCUktSc3I0SmJhQ0RZTk41YXVrbmNGTEMyRFVLc1prSW5RZ2FOcXVKOWtreU1VSkN0TWhrbzIyNVFSeGZ3cm9IQldodTRqRmoxWUtoN2krQVFuL1FmZ1JvMHFrS2ZNNFlUOC9MWmZac1piMXlVaENTRzY0TWdpR0FvS0JsU0ZnekpaQ2VJSTF5V0dWL0RLZk5UTDhhYzd4VzljQmtRUTdoZnNNOFhEYjlQbWJQYi9aTFIzZE9jWDFBc0dQeHUwOXFkUk9VK3ViK1BSYlZmM09ONFk1dkZkMkE4U3hUeExVRDNvdng0YW9RPT0=
        headers={
           'Content-Type':'multipart/form-data',
           'boundary' : '----WebKitFormBoundaryMXkAbFUIRjFzUE08',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
        files={'files':open('33.png','rb')}
        r=requests.post(url=url,headers=headers,files=files,cookies=cookies)
        print(r.cookies.values())
        print(r.text)
        assert r.status_code==200
        cookies=dict(cookies_are='working')
        r=requests.get(url,cookies=cookies)