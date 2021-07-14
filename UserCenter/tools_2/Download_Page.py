from time import sleep
from tools_1.BaseDriver import driver

def download_1():
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[6]/a').click()
    sleep(2)
    message = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]').text
    return message

# def download_2():
#     driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/p/a').click()
#     sleep(2)
#     all = driver.window_handles
#     driver.switch_to.window(all[1])
    # message = driver.find_element_by_xpath('').text
    # return message