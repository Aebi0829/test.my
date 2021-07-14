
from selenium import webdriver
import win32com.client

driver = webdriver.Chrome()#创建浏览器驱动
shell = win32com.client.Dispatch("WScript.Shell")#调用键盘驱动