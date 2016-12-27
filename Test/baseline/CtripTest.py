#usr/bin/python
#encoding:utf-8
import time
import unittest
from appium import webdriver

class MyTestCase(unittest.TestCase):
    # 脚本初始化,获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '021YHB7N3C005995'
        # desired_caps['appPackage'] = 'com.android.calculator2'
        # desired_caps['appActivity'] = '.Calculator'
        # desired_caps['appPackage'] = 'com.android.customlocale2'
        # desired_caps['appActivity'] = '.CustomLocaleActivity'
        desired_caps['appPackage'] = 'ctrip.android.view'
        desired_caps['appActivity'] = '.splash.CtripSplashActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 释放实例,释放资源
    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        time.sleep(20)
        # self.driver.find_element_by_id("call").click()
        self.driver.find_element_by_name("客服").click()
        time.sleep(5)
        # self.driver.find_element_by_id("home").click()
        self.driver.find_element_by_name("首页").click()
        time.sleep(5)
        # self.driver.find_element_by_id("home").click()
        self.driver.find_element_by_name("行程").click()
        time.sleep(5)



if __name__ == '__main__':
    unittest.main()