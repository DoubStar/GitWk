#usr/bin/python
#encoding:utf-8
import time
import unittest
from appium import webdriver

class CtripCase(unittest.TestCase):
    # 脚本初始化,获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '021YHB7N3C005995'
        desired_caps['udid'] = '021YHB7N3C005995'
        desired_caps['appPackage'] = 'ctrip.android.view'
        desired_caps['appActivity'] = '.splash.CtripSplashActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 释放实例,释放资源
    def tearDown(self):
        print '关闭'
        self.driver.quit()

    def test_something(self):
        time.sleep(8)
        # self.driver.find_element_by_id("call").click()
        print '点击我的icon'
        self.driver.find_element_by_name("我的").click()
        time.sleep(3)

        print '登录/注册'
        print self.driver.contexts

        time.sleep(5)
        # self.driver.find_element_by_id('myctrip_login_btn').click()
        self.driver.find_element_by_name('登录/注册').click()
        time.sleep(2)
        print self.driver.contexts

        if self.driver.find_element_by_name('更换账号'):
            self.driver.find_element_by_name('更换账号').click()
        time.sleep(3)
        print '输入用户名'
        self.driver.find_element_by_name('国内手机/用户名/邮箱/卡号').send_keys('18939785775')
        time.sleep(2)
        # 点击API tap的用法
        self.driver.tap([(300, 380)])
        time.sleep(2)
        self.driver.keyevent(7)
        self.driver.keyevent(7)
        self.driver.keyevent(7)
        self.driver.keyevent(8)
        self.driver.keyevent(9)
        self.driver.keyevent(10)
        self.driver.keyevent(66)

        time.sleep(10)
        print self.driver.contexts




if __name__ == '__main__':
    unittest.main()
