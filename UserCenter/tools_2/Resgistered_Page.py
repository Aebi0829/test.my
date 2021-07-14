from selenium import webdriver
from tools_2.code import get_code_1, get_code_3
from time import sleep

# alp用户中心测试环境注册
def Resgistered():

    driver = webdriver.Chrome()
    driver.get("http://client.testurls.com/login/")
    driver.maximize_window()
    sleep(4)

    code = get_code_3.yzm()
    yzm = code[0]
    phone = code[1]
    password = code[2]

    # 跳转注册界面
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[2]/span[1]/a').click()
    sleep(3)

    # 切换到注册界面
    all = driver.window_handles
    driver.switch_to.window(all[1])

    # 输入账号、密码、验证码
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/ul/li[1]/div[1]/input').send_keys(phone)
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/ul/li[2]/div[1]/input').send_keys(password)
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/ul/li[3]/div[1]/input[1]').send_keys(yzm)
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[1]/input').click()
    sleep(6)

    # # 验证注册是否成功,登录测试
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/ul/li[1]/div[1]/input').send_keys(phone)
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/ul/li[2]/div[1]/input').send_keys('qwer1234')
    sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/input').click()
    sleep(4)
    message = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/a[3]').text
    driver.quit()

    return message,phone,password