#/usr/bin/python
#encoding:utf-8
import json
import requests

URL = 'https://api.github.com'

def build_url(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    # response = requests.get(build_url('users/imoocdemo'))
    response = requests.get(build_url('user/emails'),auth=('DoubStar','shenjie1012'))
    print better_print(response.text)

if __name__ == '__main__':
    print '>>>>request_method'
    request_method()