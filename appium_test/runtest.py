#coding:UTF-8
"""
@@Time:2018.06.05  15:30
@Author:keitwo
@E-mail:
@FinleName:
#######      使用时请先打开APPIUM再执行测试    ###########
"""
import unittest,HTMLTestRunner_PY3,time

def creatsuite():
    testunit = unittest.TestSuite()
    # 设置测试文件查找的目录
    test_dir = 'D:\\work\\appium_test\\test_case'
    # 定义 discover 方法的参数
    #discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py', top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_logout.py', top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        testunit.addTests(test_suite)
    print(testunit)
    return testunit
alltestnames = creatsuite()

if __name__ == '__main__':
    report_title = u'简书app Appium自动化测试报告'
    desc = u'版本号V1.0 <br/> 作者: keitwo'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_file = 'D:\\work\\appium_test\\report\\' + now + 'result.html'
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=report, title=report_title, description=u'这是一个简书APP测试用例Demo!')
        runner.run(alltestnames)