#usr/bin/python
#encoding:utf-8
import time
import unittest
from appium import webdriver

class LifeVcCase(unittest.TestCase):
    # 脚本初始化,获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '08d356b9'
        desired_caps['udid']='08d356b9'
        desired_caps['appPackage'] = 'com.lifevc.shop'
        desired_caps['appActivity'] = '.ui.SplashActivity_'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)


    # 释放实例,释放资源
    def tearDown(self):
        print '关闭'
        self.driver.quit()

    def test_something(self):
        time.sleep(10)

        print '点击用户中心'
        self.driver.find_element_by_id('com.lifevc.shop:id/bottom_account_center').click()
        time.sleep(5)
        print '点击登录'
        self.driver.find_element_by_id('com.lifevc.shop:id/tv_login').click()
        time.sleep(2)
        print '输入用户名'
        self.driver.find_element_by_id('com.lifevc.shop:id/login_name_et').send_keys('18939785775')
        print '输入密码'
        self.driver.find_element_by_id('com.lifevc.shop:id/login_password_et').send_keys('jjllcc1981')
        print '点击确定'
        self.driver.find_element_by_id('com.lifevc.shop:id/login_btn').click()
        time.sleep(5)
        print 'end'





if __name__ == '__main__':
    unittest.main()

