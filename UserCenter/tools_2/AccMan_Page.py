from time import sleep
from selenium.webdriver.support.ui import Select
import win32com.client
from tools_1.BaseDriver import driver
from tools_2.code import get_code_1


def acc_man_1():
    # 点击'账户管理-实名认证',提交实名认证信息
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/a').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/dl/dd[1]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]/input').send_keys('test')
    s1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[3]/select')
    Select(s1).select_by_value('2')
    sleep(0.4)
    ID_number = get_code_1.ID_number()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[4]/input').send_keys(ID_number)

    # 模拟真实用户添加图片操作
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div/ul/li[1]/a').click()
    sleep(1)
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.Sendkeys('D:\\program\\program.01\\AlpUITest\\UserCenter\\picture\\test1.png'+'\r\n', 0)
    sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div/ul/li[2]/a').click()
    sleep(1)
    shell.Sendkeys('D:\\program\\program.01\\AlpUITest\\UserCenter\\picture\\test1.png' + '\r\n', 0)
    sleep(4)
    # 接口传入图片操作
    # driver.find_element_by_xpath('//*[@id="filez"]').send_keys(
    #     'D:\\program\\program.01\\alp\\user_center\\picture\\test1.png')
    # sleep(4)
    # driver.find_element_by_xpath('//*[@id="filef"]').send_keys(
    #     'D:\\program\\program.01\\alp\\user_center\\picture\\test1.png')
    # sleep(4)

    # 提交
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/input').click()
    sleep(2)

    # 验证
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/a').click()
    sleep(2)
    message = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[3]/div/p[2]').text
    return message


def acc_man_2():
    # 点击'账户管理-银行卡管理',提交银行卡信息
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/a').click()
    # sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/dl/dd[2]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/ul/li[1]/input').send_keys('test')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/ul/li[2]/input').send_keys('123456789001')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/ul/li[3]/input').send_keys('test bank')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/ul/li[5]/input').send_keys('test address')

    # 模拟真实用户添加图片操作
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/ul/li[1]/a').click()
    sleep(1)
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.Sendkeys('D:\\program\\program.01\\AlpUITest\\UserCenter\\picture\\test2.png' + '\r\n', 0)
    sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/ul/li[2]/a').click()
    sleep(1)
    shell.Sendkeys('D:\\program\\program.01\\AlpUITest\\UserCenter\\picture\\test2.png' + '\r\n', 0)
    sleep(4)

    # 提交
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/ul/input').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/a').click()
    sleep(0.4)
    message = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li/p[3]/span').text
    # 删除银行卡
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li/p[1]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/a[1]').click()
    sleep(0.4)

    return message


def acc_man_3():
    # 点击'账户管理-修改密码'，进行密码修改
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/a').click()
    # sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/dl/dd[3]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/ul/li[1]/input').send_keys('qwer1234')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/ul/li[2]/input').send_keys('1234qwer')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/ul/li[3]/input').send_keys('1234qwer')
    sleep(0.4)

    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/ul/li[1]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/ul/li[1]/a').click()
    sleep(2)
    # 提交
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/ul/input').click()
    sleep(2)
    message = driver.find_element_by_xpath('/html/body/div[6]/div[2]').text
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/a').click()
    sleep(2)

    return message
