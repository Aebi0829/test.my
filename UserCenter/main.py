import unittest
from ClassicHTMLTestRunner import HTMLTestRunner
# from HTMLTestRunner import HTMLTestRunner

# if __name__ == '__main__':
# def aq(username):
#     lp=LoginPage(driver)
#     lp.Login("13430969600","1234567a") #LoginBackstage登录
#     cp=CoursePage(driver)
#     cp.add_course("课程4",shell)
#     sleep(2)
#     lp.Login("08ze","zxy123456")
#     cp.Del_course()
#生成测试报告

if __name__ == '__main__':
    #unittest.defaultTestLoader.discover("用例所在的模块",pattern="*通配符号*.py")
    suite=unittest.defaultTestLoader.discover("testCase",pattern="DoUnittest002Home.py")
    reportFile=open(r"D:\ALPTestReport\ALP.html","wb")
    runner=HTMLTestRunner(tester="刘泽生",
                          title="测试报告",
                          description="UI自动化测试报告",
                          stream=reportFile,
                          verbosity=2)
    runner.run(suite)