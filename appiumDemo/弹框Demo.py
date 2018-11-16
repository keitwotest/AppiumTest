#coding:utf-8
from appium import webdriver
from time import sleep
desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '4.4.2',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)
# 点弹出框去看看
driver.tap([(374, 831), (654, 906)], 500)

# 返回上一页
driver.back()
sleep(2)

# 点右上角搜素按钮
driver.tap([(615, 52), (690, 146)], 500)