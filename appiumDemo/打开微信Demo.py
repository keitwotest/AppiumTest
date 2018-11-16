#coding=utf-8
from appium import webdriver

import time
#appium 微信h5自动化示例
packageName='com.tencent.mm'
appActivity='.ui.LauncherUI'
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'MI 5s'
desired_caps['appPackage'] = packageName
desired_caps['appActivity'] = appActivity
desired_caps['waitappActivity'] = '.activity.login.VerifyActivity'
desired_caps['fullReset'] = 'false'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['fastReset'] = 'false'
desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}   #驱动H5自动化关键之一

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)
#driver.find_element_by_name('我').click()
driver.find_element_by_name('发现').click()
print driver.contexts
#driver.find_element_by_name('相册').click()
driver.find_element_by_name('小程序').click()
# driver.find_element_by_xpath("//*[contains(@text,'正在繁星直播')]").click()
# print driver.current_context
# driver.find_element_by_xpath("//*[contains(@text,'正在繁星直播')]").click()
# print driver.current_context
# driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
# print driver.current_context
# print driver.page_source