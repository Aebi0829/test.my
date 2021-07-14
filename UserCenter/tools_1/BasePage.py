from tools_1.config import HOST
class BasePage():#用于封装公共方法
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)
        self.driver.get(HOST)
        self.driver.maximize_window()

        # 点击操作--知道元素的定位方法
    def click_element1(self, locator):
        self.driver.find_element(locator[0], locator[1]).click()
#locator内，locator[0]为定位元素的方法，locator[1]为元素的位置
#css 方法名：css selector
#xpath 方法名：xpath
#id 方法名：id

        # 输入操作--知道元素的定位方法还有文本
    def input_text(self, locator, text):
        self.driver.find_element(locator[0], locator[1]).send_keys(text)

        # 获取元素-复数形式
    def get_webelements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])