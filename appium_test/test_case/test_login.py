#coding:UTF-8
"""
@@Time:2018.06.05  15:30
@Author:keitwo
@E-mail:
@FinleName:
"""
import time,unittest
from appium import webdriver
from config import driver_configure

index = 1  #和截图有关

class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'  # 设备系统
        # desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
        # desired_caps['deviceName'] = '127.0.0.1:62001'  # 设备名称
        # desired_caps['appPackage'] = 'com.jianshu.haruki'  # 测试app包名
        # desired_caps['appActivity'] = 'com.baiji.jianshu.ui.splash.SplashScreenActivity'  # 测试appActivity
        # desired_caps['noReset'] = 'true'
        # #desired_caps['app'] = 'D:\\work\\appium\\jianshu.apk',
        # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()

    @classmethod
    def tearDownClass(cls):
        global index
        cls.screenshot(index)
        index += 1

        cls.driver.quit()

    png_file = "D:\\work\\appium_test\\report\\"  # 图片存放地址,这个地址要想创建好
    def screenshot(self, index):  # 需要写这个方法才能实现截图
        #timestr = time.strftime('%Y%m%d', time.localtime(time.time()))  # 精确到秒会无法截图，要和htmltestrunner.py文件格式一致
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        img_name = timestr + '_' + str(index) + '.png'  # 图片以时间+第几次截图命名
        self.driver.get_screenshot_as_file('%s%s' % (self.png_file, img_name))  # 图片保存在定义路径中
        return img_name

    def test_login(self):
        """登录简书APP-测试用例"""
        driver = self.driver
        # 休眠五秒等待页面加载完成
        time.sleep(3)
        driver.find_element_by_id("com.jianshu.haruki:id/tab_more").click()
        time.sleep(2)
        driver.find_element_by_id("com.jianshu.haruki:id/item_user").click()
        time.sleep(3)
        self.screenshot(index)
        driver.find_element_by_id("com.jianshu.haruki:id/et_account").send_keys("xxxxx@qq.com")
        time.sleep(3)
        driver.find_element_by_id("com.jianshu.haruki:id/et_password").send_keys("xxxxxx")
        time.sleep(3)
        driver.find_element_by_id("com.jianshu.haruki:id/btn_login").click()
        time.sleep(2)
        name = driver.find_element_by_id('com.jianshu.haruki:id/text_user_name').text
        time.sleep(3)
        self.screenshot(index)
        try:   # 添加断言，若昵称不正确，则打印错误信息
            assert 'keitwo' in name
            print('loginUser is right')
        except AssertionError as e:
            driver.get_screenshot_as_file('D:\\work\\appium\\report\\' + time.strftime("%Y-%m-%d %H_%M_%S") +'.png')
            print('loginUser is Error')

    def test_logout(self):
        """退出简书APP-测试用例"""
        driver = self.driver
        driver.find_element_by_id("com.jianshu.haruki:id/iv_setting").click()
        time.sleep(2)
        self.swipeUp(1000)
        time.sleep(5)
        self.screenshot(index)
        driver.find_element_by_id("com.jianshu.haruki:id/tv_logout").click()
        time.sleep(3)
        self.screenshot(index)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout").find_element_by_name(u"是").click()

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

