#coding:utf-8
from appium import webdriver
import time
desired_caps = {'platformName': 'Android',
                'deviceName': '30d4e606',
                'platformVersion': '6.0',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(30)
# 点图书按钮
driver.find_element_by_id("com.baidu.yuedu:id/righttitle").click()
time.sleep(3)
# 切换到图书界面后获取所有的环境
contexts = driver.contexts
print(contexts)

# 切换到webview
driver.switch_to.context(contexts[1])
# 获取当前的环境，看是否切换成功
now = driver.current_context
print(now)

# 切回native
driver.switch_to.context(contexts[0])
# driver.switch_to.context("NATIVE_APP") # 这样也是可以的
# 获取当前的环境，看是否切换成功
now = driver.current_context
print(now)