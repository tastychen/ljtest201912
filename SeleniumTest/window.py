import time
from selenium import webdriver
#导入webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:9999/shopxo")

# 在首页点击小姐姐
xiaojiejie = ("xpath", '//*[@id="floor1"]/div[2]/div[2]/div[2]/a/img')
find_element(driver, xiaojiejie).click()

print(driver.title)
driver.switch_to_window(driver.window_handles[-1])


# 新窗口点击购买
buy = ("xpath", '/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button')
find_element(driver, buy).click()
print(driver.title)
