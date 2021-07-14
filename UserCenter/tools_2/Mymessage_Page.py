from selenium.webdriver.support.ui import Select
from time import sleep
from tools_1.BaseDriver import driver

def my_message_1():
    # 我的消息模块 用例--筛选我的消息
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[7]/a').click()
    sleep(2)
    s1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/select')
    # 交易安排
    Select(s1).select_by_value('62D744AF-91C6-425D-A612-76DcaD046E6D')
    sleep(2)
    # 存取款通知
    Select(s1).select_by_value('62D744AF-91C6-425D-A612-76DcaD046E1D')
    sleep(2)
    # 维护通知
    Select(s1).select_by_value('62D744AF-91C6-425D-A612-76DcaD146E1D')
    sleep(2)
    # 重要公告
    Select(s1).select_by_value('62D744AF-91C6-425D-A612-76D5CD046E6D')
    sleep(2)

def my_message_2():
    # 我的消息模块 用例--点击我的消息的内容
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/a').click()
    sleep(2)
    message = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[3]/p/span').text
    return message

def my_message_3():
    # 我的消息模块 用例--点击返回消息列表
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/a').click()
    sleep(2)
    message = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]').text
    return message