from time import sleep
from tools_1.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        #首页的登录按钮
        # self.login_btn='css selector','.sub input'
        self.username_input='xpath',"/html/body/div[2]/div/div/div[2]/form/ul/li[1]/div[1]/input"
        self.password_input='xpath',"/html/body/div[2]/div/div/div[2]/form/ul/li[2]/div[1]/input"
        #登录页的登录按钮
        self.loginpage_btn='css selector',".sub input"
        #进入按钮
        self.backstage='css selector',".top-menu .normal"
    def Login(self,username,password):#登录并进入前端
        self.input_text(self.username_input,username)
        sleep(2)
        self.input_text(self.password_input,password)
        sleep(2)
        self.click_element1(self.loginpage_btn)
        sleep(2)









        # driver.implicitly_wait(1)
        # eles=driver.find_elements_by_css_selector(".sub input")
        # if eles: #如果页面有这个登录按钮的元素则点击，没有的话就没有
        #     self.click_element1(self.login_btn)
        # driver.implicitly_wait(1)