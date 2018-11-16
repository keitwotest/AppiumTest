#coding:UTF-8
"""
@@Time:2018.06.05  15:30
@Author:keitwo
@E-mail:
@FinleName:
"""
import unittest,time
from appium import webdriver
from config import driver_configure

class logoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

    def test_logout(self):
        """退出简书APP-测试用例"""
        driver = self.driver
        driver.find_element_by_id("com.jianshu.haruki:id/iv_setting").click()
        time.sleep(2)
        driver = self.swipeUp()
        time.sleep(2)
        driver.get_screenshot_as_file('D:\\work\\appium\\report\\' + time.strftime("%Y-%m-%d %H_%M_%S") + '.png')
        driver.find_element_by_id("com.jianshu.haruki:id/tv_logout").click()
        time.sleep(2)
        driver.switch_to_alert()  #定位弹框
        driver.find_element_by_name(u'是').click()

    def getSize(self):  # 获取屏幕宽和高
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeUp(self, t):  # 向上滑动
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, t)