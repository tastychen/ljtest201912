import time
from selenium import webdriver
#导入webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:9999/shopxo/admin.php")

username = ("name", "username")
password = ("name", "login_pwd")
loginbtn = ("xpath", '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')

find_element(driver, username).send_keys("admin")
find_element(driver, password).send_keys("shopxo")
find_element(driver, loginbtn).click()

# 切换作用域到iframe子网页中
iframe = ("id", "ifcontent")
driver.switch_to_frame(find_element(driver, iframe))

user_account = ("xpath", '/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
a = find_element(driver, user_account).text
print(a)