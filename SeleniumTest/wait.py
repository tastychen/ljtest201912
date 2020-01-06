import time
from selenium import webdriver
#导入webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:9999/shopxo/")

# 动态查询找元素，driver浏览器操作对象， 10：超时时间

# 用元祖存放定位方式
search_input = ("id", "search-input") #*search_input="id", "search-input"
ai_topsearch = ("id", "ai-topsearch")
goods_prices = ("xpath", '/html/body/div[4]/div/ul/li/div/p[2]/strong')

find_element(driver, search_input).send_keys("纽芝兰")
find_element(driver, ai_topsearch).click()
assert find_element(driver, goods_prices).text == "￥168.00"

# 获取网页的title和url
print("网页的title是", driver.title)
print("网页的地址是", driver.current_url)
# # 操作元素
# WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input)).send_keys("纽芝兰")
# WebDriverWait(driver, 10).until(lambda s: s.find_element(*ai_topsearch)).click()
# e = WebDriverWait(driver, 10).until(lambda s: s.find_element(*goods_prices))
# assert "￥168.00" == e.text
# print("成功！")



