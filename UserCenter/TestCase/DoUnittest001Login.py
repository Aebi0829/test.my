# -*- coding:utf-8 -*-
import unittest
from tools_1.BaseDriver import driver

from tools_2.Login_Page import LoginPage

class LoginTest(unittest.TestCase,LoginPage):
    def setUp(self):
        print('---test start!---')
    def tearDown(self):
        self.driver = driver
        self.driver.quit()
        print('---test end!---')

    def test_001(self):
        # 用例1--登录正确的账号密码
        lp=LoginPage(driver)
        # LoginBackstage登录
        lp.Login("13430969600","1234567a")
        a=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]").get_attribute('textContent')
        self.assertEqual(a,"欢迎，134****9600","未成功")
        print('登录用例执行成功')

