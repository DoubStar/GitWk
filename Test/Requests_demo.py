
# _*_ coding: utf-8 _*_
import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text

def use_params_requests():
    #构建一个请求参数
    params = {'param1':'hello','param2':'world'}
    response = requests.get(URL_GET,params=params)

    print '>>>>Response Headers:'
    print response.headers
    print '>>>Status code'
    print response.status_code
    print '>>>>Response Body'
    print response.json()



if __name__ =='__main__':
    print '>>>Use simple urllib2'
    use_simple_requests()
    print
    print '>>>Use param requests'
    use_params_requests()