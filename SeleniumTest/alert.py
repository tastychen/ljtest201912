import time
from selenium import webdriver
#导入webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost:8080/test/")

demo1 = ("link text", "点我就送屠龙宝刀！")
find_element(driver, demo1).click()
time.sleep(2)
# 处理弹窗按钮
driver.switch_to_alert().accept()   # 点确定按钮

demo2 = ("link text", "点我就送251天免费套餐+10W！")
find_element(driver, demo2).click()
time.sleep(2)
driver.switch_to_alert().dismiss()

 
