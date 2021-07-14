import unittest
import warnings
from tools_2.Login_Page import LoginPage
from tools_2 import Resgistered_Page

class LoginTest(unittest.TestCase,LoginPage):
    def setUp(self):
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)
        print('---test start!---')
    def tearDown(self):
        # self.driver = driver
        # self.driver.quit()
        print('---test end!---')

    def test_res(self):
        message = Resgistered_Page.Resgistered()[0]
        self.assertEqual(message,'退出登录')
        print('注册用例执行完成')


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
"""
注：实名注册中包含注册流程，此文件可单独执行注册
"""