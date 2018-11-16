#coding=utf-8
from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',  #android apk还是IOS apk
    'deviceName': '127.0.0.1:62001',   #手机设备名称，通过 adb devices 查看
    'platformVersion': '5.0',  #android 系统的版本号
    'appPackage': 'com.taobao.taobao',  #apk 包名
    'appActivity':'com.taobao.tao.welcome.Welcome',  #apk 的 launcherActivity
    'unicodeKeyboard': True,   #使用unicode编码方式发送字符串
    'resetKeyboard': True,  #将键盘隐藏起来
    'app' :'D:/work/appium/shoujitaobao_174.apk'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# 休眠五秒等待页面加载完成
time.sleep(50)
#driver.find_element_by_link_text('手机淘宝')
#driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
#time.sleep(10)
#driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
#time.sleep(5)
#driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("keitwo")

