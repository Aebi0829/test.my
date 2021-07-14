# -*- coding:utf-8 -*-
from time import sleep
import unittest

timesec=2
#切换浏览器页签
# all = self.driver.window_handles
# self.driver.switch_to.window(all[1])  （切换第一个 输入0）
from lib.Login_Page import LoginPage
class LoginTest(unittest.TestCase,LoginPage):
    def setUp(self):
        print('---test start!---')
        # self.driver = webdriver.Ie(executable_path=driverfile_path)
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://client.testurls.com/login/")
        # self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print('---test end!---')

    def testLogin1(self,username,password):
        # 用例1--登录正确的账号密码
        self.Login(username,password)
        # account = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/ul/li[1]/div[1]/input')
        # password = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/ul/li[2]/div[1]/input')
        # account.send_keys(username)
        # sleep(0.4)
        # password.send_keys(password)
        # sleep(0.4)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/input').click()
        # sleep(2)
        # message = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]').text
        # self.assertEqual(message, '欢迎，test-aebi13212')
        # sleep(4)
        print('用例1执行完成')
if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(LoginTest('testLogin1'))
    # suite.addTest(LoginTest('testLogin2'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
#登录