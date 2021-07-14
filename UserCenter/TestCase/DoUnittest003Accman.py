import unittest
import warnings
from tools_1.BaseDriver import  driver
from tools_2 import Resgistered_Page
from tools_2.Login_Page import LoginPage
from tools_2 import AccMan_Page

class TestAccount(unittest.TestCase,LoginPage):

    @classmethod
    # 执行第一个用例前执行
    def setUpClass(cls):
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)
        print('---test start!---')

    @classmethod
    # 执行所有用例之后执行
    def tearDownClass(cls):
        cls.driver = driver
        cls.driver.quit()
        print('---test end!---')

    # def setUp(self):
    #     # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
    #     warnings.simplefilter('ignore', ResourceWarning)
    #     print('---test start!---')
    #
    # def tearDown(self):
    #     # self.driver = driver
    #     # self.driver.quit()
    #     print('---test end!---')

    def test_acc_man_1(self):
        # 用例1--注册+实名认证
        # 获取账号密码
        message1 = Resgistered_Page.Resgistered()
        self.assertEqual(message1[0], '退出登录')
        print('注册用例执行完成')
        phone = message1[1]
        password = message1[2]
        lp = LoginPage(driver)
        lp.Login(phone,password)
        message2 = AccMan_Page.acc_man_1()
        self.assertEqual(message2,'您好！您的实名认证信息已提交，请耐心等待审核。')
        print('账户管理用例1执行成功')

    def test_acc_man_2(self):
        # 用例2--银行卡添加/删除
        message = AccMan_Page.acc_man_2()
        self.assertEqual(message,'待审核')
        print('账户管理用例2执行成功')

    def test_acc_man_3(self):
        # 用例3--密码修改
        message = AccMan_Page.acc_man_3()
        self.assertEqual(message,'密码修改成功')
        print('账户管理用例3执行成功')


if __name__ == '__main__':
    unittest.main(verbosity=2)