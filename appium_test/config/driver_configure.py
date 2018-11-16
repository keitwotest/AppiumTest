#coding:UTF-8
"""
@@Time:2018.06.05  15:30
@Author:keitwo
@E-mail:
@FinleName:
"""
from appium import webdriver

class driver_configure():
    def get_driver(self):
        """"获取driver"""
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 设备系统
            self.desired_caps['platformVersion'] = '5.1'  # 设备系统版本 4.4.2    7.0
            self.desired_caps['deviceName'] = '106D111805004868'  # 设备名称  127.0.0.1:62001    d015fa0e
            self.desired_caps['appPackage'] = 'com.jianshu.haruki'  # 测试app包名
            self.desired_caps['appActivity'] = 'com.baiji.jianshu.ui.splash.SplashScreenActivity'  # 测试appActivity
            self.desired_caps['noReset'] = 'true'
            # desired_caps['app'] = 'D:\\work\\appium\\jianshu361.apk',
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
            return self.driver
        except Exception as e:
            raise e