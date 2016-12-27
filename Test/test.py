
# _*_ coding: utf-8 _*_
import urllib2
import urllib

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print '>>>>Response Headers:'
    print response.info()

    print '>>>>Response Body:'
    text = ''.join([line for line in response.readlines()])
    # text = response.readlines()
    print text

def use_params_urllib2():
    #构建一个请求参数
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print 'Request Params:'
    print params
    response = urllib2.urlopen('?'.join([URL_GET,'%s'])%params)

    print '>>>>Response Headers:'
    print response.info()
    print '>>>>>Response status code:'
    print response.getcode()
    print '>>>>Response Body:'
    text = ''.join([line for line in response.readlines()])
    # text = response.readlines()
    print text


if __name__ =='__main__':
    print '>>>Use simple urllib2'
    use_simple_urllib2()
    print
    print '>>>Use param urllib2'
    use_params_urllib2()