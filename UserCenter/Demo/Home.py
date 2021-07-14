

from selenium import webdriver
from time import sleep
# from tools_1.BasePage import BasePage
# from tools_1.BaseDriver import driver
# import logging

timesec=2

#切换浏览器页签
# all = self.driver.window_handles
# self.driver.switch_to.window(all[1])  （切换第一个 输入0）

driver=webdriver.Chrome(r"C:\Users\sunjinlin\AppData\Local\Google\Chrome\Application\chromedriver.exe")#创建浏览器驱动
driver.implicitly_wait(10)
driver.get("http://client.testurls.com/")
driver.maximize_window()
#登录
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/ul/li[1]/div[1]/input").send_keys("13430969600")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/ul/li[2]/div[1]/input").send_keys("1234567a")
driver.find_element_by_css_selector(".sub input").click()
sleep(timesec)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]").get_attribute('textContent')
all = driver.window_handles
# a = driver.current_window_handle


#
# # 点击左上角logo
# driver.find_element_by_css_selector(".logo").click()

# sleep(timesec)
# driver.switch_to.window(all[0])
# print("Logo跳转官网成功")
# #点击返回ALP官网
# sleep(timesec)
# driver.find_element_by_css_selector(".jiaoyi").click()
# sleep(timesec)
# driver.switch_to.window(all[0])
# print("返回官网成功")
#点击在线客服
sleep(timesec)
driver.find_elements_by_css_selector(".kefu")[0].click()

sleep(timesec)
sleep(3)
all = driver.window_handles
driver.switch_to.window(all[1])  
mark = driver.find_element_by_xpath('//*[@id="ec--cs-root"]/div/div[1]/div[2]/p[2]').text
print("mark", mark)
driver.switch_to.window(all[0])
print("客服进入成功1")
sleep(timesec)
driver.find_elements_by_css_selector(".kefu")[1].click()
sleep(timesec)
driver.switch_to.window(all[0])
print("客服进入成功2")
sleep(timesec)
# #邀请好友-一键复制
# driver.find_elements_by_css_selector(".iyqhy .btn")[0].click()
# sleep(timesec)
#
# a=driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
# print("a=",a)
# print(type(a))
# sleep(timesec)
# driver.find_element_by_css_selector(".layui-layer-btn0").click()
# sleep(timesec)
# driver.find_elements_by_css_selector(".iyqhy .btn")[1].click()
# sleep(timesec)
# driver.find_element_by_css_selector(".layui-layer-btn0").click()
# sleep(timesec)
# print("一键复制点击成功")
#
# #点击入金按钮
# driver.find_elements_by_css_selector(".ubot .btnbox a")[0].click()
# sleep(timesec)
# #返回首页
# driver.find_elements_by_css_selector(".fa")[0].click()
# sleep(timesec)
# print("入金跳转成功")
# #点击出金按钮
# driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div/a[2]").click()
# sleep(timesec)
# #返回首页
# driver.find_elements_by_css_selector(".fa")[0].click()
# sleep(timesec)
# print("出金跳转成功")
#

driver.quit()