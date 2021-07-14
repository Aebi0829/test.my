from time import sleep
from tools_1.BasePage import BasePage
from tools_1.BaseDriver import driver
import logging
class HomePage(BasePage):
    all = driver.window_handles
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        all = self.driver.window_handles
    def logo_jump(self):
        # 点击左上角logo
        self.driver.find_element_by_css_selector(".logo").click()
        sleep(2)
        all = driver.window_handles
        driver.switch_to.window(all[-1])
        mark = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[1]').text
        print(mark)
        # 返回ALP官网
        self.driver.switch_to.window(all[0])
        sleep(2)
        # mark标记：联系电话 4001200095
        return mark
    def return_official_website_jump(self):
        #返回ALP官网跳转
        self.driver.find_element_by_css_selector(".jiaoyi").click()
        sleep(2)
        all = driver.window_handles
        driver.switch_to.window(all[-1])
        #mark标记：联系电话 4001200095
        mark = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[1]').text
        print(mark)
        sleep(2)
        self.driver.switch_to.window(all[0])
        sleep(2)
        return mark
    def customer_service_jump(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/a[2]/i").click()
        sleep(2)
        #新页签时，要跳转到第二个页签后才能抓第二个页签的数据
        all = driver.window_handles
        driver.switch_to.window(all[-1])
        #mark标记：EC在线客服竭诚为您服务
        mark1=self.driver.find_element_by_xpath('//*[@id="ec--cs-root"]/div/div[1]/div[2]/p[2]').text
        sleep(2)
        self.driver.switch_to.window(all[0])
        print("客服进入成功1")
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='app']/div[4]/div[2]/a/p[1]/img").click()
        sleep(2)
        all = driver.window_handles
        driver.switch_to.window(all[-1])
        sleep(2)
        mark2=self.driver.find_element_by_xpath('//*[@id="ec--cs-root"]/div/div[1]/div[2]/p[2]').text
        self.driver.switch_to.window(all[0])
        print("客服进入成功2")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/ul/li[3]/a").click()
        sleep(2)
        all = driver.window_handles
        driver.switch_to.window(all[-1])
        sleep(2)
        mark3 = self.driver.find_element_by_xpath('//*[@id="ec--cs-root"]/div/div[1]/div[2]/p[2]').text
        self.driver.switch_to.window(all[0])
        print("客服进入成功3")
        sleep(2)

        return mark1,mark2,mark3
    def invite_friends(self):
        #邀请好友-一键复制
        self.driver.find_elements_by_css_selector(".iyqhy .btn")[0].click()
        sleep(1)
        # mark标记：复制成功
        mark1=self.driver.find_element_by_xpath('//*[@class="layui-layer-content"]').text
        sleep(1)
        self.driver.find_element_by_css_selector(".layui-layer-btn0").click()
        sleep(1)
        self.driver.find_elements_by_css_selector(".iyqhy .btn")[1].click()
        sleep(1)
        # mark标记：复制成功
        mark2 = self.driver.find_element_by_xpath('//*[@class="layui-layer-content"]').text
        sleep(1)
        self.driver.find_element_by_css_selector(".layui-layer-btn0").click()
        sleep(1)
        # print("一键复制点击成功")
        return mark1,mark2
    def golden_jump(self):
        #点击入金按钮
        self.driver.find_elements_by_css_selector(".ubot .btnbox a")[0].click()
        sleep(2)
        #mark标记：选择入金金额（美金）
        mark1=self.driver.find_element_by_xpath('//*[@id="app"]/div[3]').text
        #返回首页
        self.driver.find_elements_by_css_selector(".fa")[0].click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/ul/li[1]/a").click()
        sleep(2)
        mark2 = self.driver.find_element_by_xpath('//*[@id="app"]/div[3]').text
        sleep(2)
        self.driver.find_elements_by_css_selector(".fa")[0].click()

        return mark1,mark2
    def withdraw_jump(self):
        #点击出金按钮
        self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div/a[2]").click()
        sleep(2)
        # mark标记：输入出金金额（美金）
        mark1 = self.driver.find_element_by_xpath('//*[@id="app"]/div[3]').text
        sleep(2)
        #返回首页
        self.driver.find_elements_by_css_selector(".fa")[0].click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/ul/li[2]/a").click()
        sleep(2)
        mark2 = self.driver.find_element_by_xpath('//*[@id="app"]/div[3]').text
        self.driver.find_elements_by_css_selector(".fa")[0].click()
        return mark1,mark2
    def download_jump(self):
        #点击平台下载按钮
        self.driver.find_element_by_xpath("/html/body/div[3]/ul/li[4]/a").click()
        sleep(2)
        # mark标记：平台下载
        mark = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]').text
        sleep(2)
        #返回首页
        self.driver.find_elements_by_css_selector(".fa")[0].click()
        sleep(2)
        return mark
    def banner_jump(self):
        #点击banner
        self.driver.find_element_by_xpath("//*[@id='app']/div[3]/div/div/div[3]").click()
        sleep(2)
        all = driver.window_handles
        driver.switch_to.window(all[-1])
        sleep(2)
        # mark标记：关于百度
        mark = self.driver.find_element_by_xpath('//*[@id="bottom_layer"]/div/p[2]/a').text
        sleep(2)
        self.driver.switch_to.window(all[0])
        sleep(2)
        return mark
    def message_jump(self):
        #点击banner
        self.driver.find_element_by_xpath("//*[@id='app']/div[4]/div[1]/ul/li[1]/a").click()
        sleep(2)
        # mark标记：返回消息列表
        mark = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/a').text
        sleep(2)
        self.driver.find_elements_by_css_selector(".fa")[0].click()
        sleep(2)
        return mark