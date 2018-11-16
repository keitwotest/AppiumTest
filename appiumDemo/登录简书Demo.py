#coding:UTF-8
from appium import webdriver
import time,os,unittest,HTMLTestRunner

desired_caps = {
    'platformName': 'Android',  #android apk还是IOS apk
    'deviceName': '127.0.0.1:62001',   #手机设备名称，通过 adb devices 查看
    'platformVersion': '5.0',  #android 系统的版本号
    'appPackage': 'com.jianshu.haruki',  #apk 包名
    'appActivity':'com.baiji.jianshu.ui.splash.SplashScreenActivity',  #apk 的 launcherActivity
    'unicodeKeyboard': True,   #使用unicode编码方式发送字符串
    'resetKeyboard': True,  #将键盘隐藏起来
    'app' :'D:/work/appium/jianshu.apk',
    'noReset':True ,
    'fullReset':False
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# 休眠五秒等待页面加载完成
time.sleep(10)
driver.find_element_by_id("com.jianshu.haruki:id/iv_mine").click()
time.sleep(5)
driver.find_element_by_id("com.jianshu.haruki:id/item_user").click()
time.sleep(3)
driver.find_element_by_id("com.jianshu.haruki:id/et_account").send_keys("xxxxx@qq.com")
time.sleep(3)
driver.find_element_by_id("com.jianshu.haruki:id/et_password").send_keys("xxxxx")
time.sleep(3)
driver.find_element_by_id("com.jianshu.haruki:id/btn_login").click()
time.sleep(2)
name = driver.find_element_by_id('com.jianshu.haruki:id/text_user_name').text
# 添加断言，若昵称不正确，则打印错误信息
try:
    assert 'keitwo' in name
    print('loginUser is right')
except AssertionError as e:
    print('loginUser is Error')

