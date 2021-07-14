import unittest
from time import sleep
from tools_1.BaseDriver import driver
#---执行用例---

def fun_man_1():
    # 点击'资金管理-入金'，进行银行卡入金操作
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/a').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/dl/dd[1]/a').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[5]/input').send_keys('201')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[7]/ul/li[3]/p[2]/em').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/input').click()
    sleep(2)
    all = driver.window_handles
    driver.switch_to.window(all[1])
    driver.find_element_by_xpath('/html/body/div/div/div[5]/div[2]/button').click()
    sleep(3)
    message = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[4]/button').text
    # 一键购买
    return message

def fun_man_2():
    # 点击'资金管理-出金'，进行出金操作(需要用户已完成实名认证、已绑银行卡)
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/a').click()
    # sleep(0.4)
    all = driver.window_handles
    driver.switch_to.window(all[0])
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/dl/dd[2]').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[4]/input').send_keys('25')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul[2]/li/select/option[2]').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/input[1]').click()
    sleep(3)
    message = driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]').text
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/a').click()
    sleep(3)
    # 出金申请已提交，请耐心等待...
    return message

def fun_man_3():
    # 点击'资金管理-资金明细',进行数据查询
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/a').click()
    # sleep(0.4)
    all = driver.window_handles
    driver.switch_to.window(all[0])
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/dl/dd[3]/a').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li/div/input[1]').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/button[4]').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li/select/option[1]').click()
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li/input').click()
    sleep(3)
    message = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]').text
    # 25
    return message


if __name__ == '__main__':
    unittest.main(verbosity=2)