import unittest
import warnings
from tools_1.BaseDriver import  driver
from tools_2.Login_Page import LoginPage
from tools_2 import Mymessage_Page
from tools_2 import Download_Page

class TestMessage(unittest.TestCase,LoginPage):

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

    def test_download_1(self):
        # 平台下载用例1--点击平台下载界面
        lp = LoginPage(driver)
        lp.Login('13066660018', 'qwer1234')
        message = Download_Page.download_1()
        self.assertEqual(message,'平台下载')
        print('平台下载用例1执行完成')

    # def test_download_2(self):
    #     # 平台下载用例1--点击平台下载界面
    #     message = Download_Page.download_2()
    #     self.assertEqual(message, '')
    #     print('平台下载用例2执行完成')

    def test_my_message_1(self):
        # 我的消息用例1--筛选我的消息的内容
        Mymessage_Page.my_message_1()
        print('我的消息用例1执行完成')

    def test_my_message_2(self):
        # 我的消息用例1--查看我的消息的内容
        message = Mymessage_Page.my_message_2()
        self.assertEqual(message,'分类： 重要公告')
        print('我的消息用例2执行完成')

    def test_my_message_3(self):
        # 我的消息用例1 - -返回我的消息的界面
        message = Mymessage_Page.my_message_3()
        self.assertEqual(message,'我的消息')
        print('我的消息用例3执行完成')



if __name__ == '__main__':
    unittest.main(verbosity=2)