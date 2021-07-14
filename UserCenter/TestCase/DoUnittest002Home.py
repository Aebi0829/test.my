# -*- coding:utf-8 -*-
import unittest
from tools_1.BaseDriver import  driver

from tools_2.Home_Page import HomePage
from tools_2.Login_Page import LoginPage
class HomeTest(unittest.TestCase,HomePage,LoginPage):
    @classmethod
    def setUpClass(cls):
        print('---test start!---')
        # lp1=LoginPage(driver)
        # print(111111111111)
        # lp1.Login("13430969600","1234567a") #LoginBackstage登录
    @classmethod
    def tearDownClass(cls):
        cls.driver=driver
        cls.driver.quit()
        print('---test end!---')

    def test_001(self):
        # 用例1--登录正确的账号密码
        lp=LoginPage(driver)
        # LoginBackstage登录
        lp.Login("13430969600","1234567a")
        print('登录成功')
    def test_002(self):
        # 用例3--登录左上角logo跳转
        lp=HomePage(driver)
        # logo跳转
        mark=lp.logo_jump()
        self.assertEqual(mark,"联系电话 4001200095","未成功")
        print('logo跳转成功')
    def test_003(self):
        # 用例4--返回ALP官网跳转
        lp=HomePage(driver)
        mark=lp.return_official_website_jump()
        self.assertEqual(mark,"联系电话 4001200095","未成功")
        print('返回ALP官网跳转成功')
    def test_004(self):
        # 用例2--验证首页两个在线客服跳转
        lp=HomePage(driver)
        # 客服跳转
        mark=lp.customer_service_jump()
        self.assertEqual(mark[0],"EC在线客服竭诚为您服务","未成功")
        print('客服1跳转成功')
        self.assertEqual(mark[1], "EC在线客服竭诚为您服务", "未成功")
        print('客服2跳转成功')
        self.assertEqual(mark[2], "EC在线客服竭诚为您服务", "未成功")
        print('客服3跳转成功')
    def test_005(self):
        # 用例5--邀请好友复制按钮点击
        lp=HomePage(driver)
        mark=lp.invite_friends()
        self.assertEqual(mark[0],"复制成功","未成功")
        self.assertEqual(mark[1],"复制成功","未成功")
        print('邀请好友复制成功')
    def test_006(self):
        # 用例6--入金按钮跳转
        lp=HomePage(driver)
        mark=lp.golden_jump()
        self.assertEqual(mark[0],"选择入金金额（美金）","未成功")
        self.assertEqual(mark[1],"选择入金金额（美金）", "未成功")
        print('入金按钮跳转成功')
    def test_007(self):
        # 用例7--出金按钮跳转
        lp=HomePage(driver)
        mark=lp.withdraw_jump()
        self.assertEqual(mark[0],"输入出金金额（美金）","未成功")
        self.assertEqual(mark[1],"输入出金金额（美金）","未成功")
        print('出金按钮跳转成功')
    def test_008(self):
        # 用例8--平台下载按钮跳转
        lp=HomePage(driver)
        mark=lp.download_jump()
        self.assertEqual(mark,"平台下载","未成功")
        print('平台下载按钮跳转成功')
    def test_009(self):
        # 用例9--banner跳转
        lp=HomePage(driver)
        mark=lp.banner_jump()
        self.assertEqual(mark,"关于百度","未成功")
        print('banner跳转成功')
    def test_010(self):
        # 用例10--消息详情跳转
        lp=HomePage(driver)
        mark=lp.message_jump()
        self.assertEqual(mark,"返回消息列表","未成功")
        print('消息详情跳转成功')
    # def test_002(self):
    #     # 用例1--登录正确的账号密码
    #     lp=HomePage(driver)
    #     driver.implicitly_wait(10)
    #     mark=lp.customer_service_jump() #logo跳转
    #     self.assertEqual(mark,"EC在线客服竭诚为您服务","未成功")
    #     print('客服跳转成功')
    # def test_002(self):
    #     # 用例1--登录正确的账号密码
    #     lp=HomePage(driver)
    #     driver.implicitly_wait(10)
    #     mark=lp.customer_service_jump() #logo跳转
    #     self.assertEqual(mark,"EC在线客服竭诚为您服务","未成功")
    #     print('客服跳转成功')
    # def test_002(self):
    #     # 用例1--登录正确的账号密码
    #     lp=HomePage(driver)
    #     driver.implicitly_wait(10)
    #     mark=lp.customer_service_jump() #logo跳转
    #     self.assertEqual(mark,"EC在线客服竭诚为您服务","未成功")
    #     print('客服跳转成功')
    # def test_002(self):
    #     # 用例1--登录正确的账号密码
    #     lp=HomePage(driver)
    #     driver.implicitly_wait(10)
    #     mark=lp.customer_service_jump() #logo跳转
    #     self.assertEqual(mark,"EC在线客服竭诚为您服务","未成功")
    #     print('客服跳转成功')
    # def test_002(self):
    #     # 用例1--登录正确的账号密码
    #     lp=HomePage(driver)
    #     driver.implicitly_wait(10)
    #     mark=lp.customer_service_jump() #logo跳转
    #     self.assertEqual(mark,"EC在线客服竭诚为您服务","未成功")
    #     print('客服跳转成功')
    # def test_002(self):
    #     # 用例1--登录正确的账号密码
    #     lp=HomePage(driver)
    #     driver.implicitly_wait(10)
    #     mark=lp.customer_service_jump() #logo跳转
    #     self.assertEqual(mark,"EC在线客服竭诚为您服务","未成功")
    #     print('客服跳转成功')