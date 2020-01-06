import time
from selenium import webdriver
#导入webdriverwait

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:9999/shopxo/")

# 搜索纽芝兰包包
driver.find_element_by_id("search-input").send_keys("纽芝兰")
driver.find_element_by_id("ai-topsearch").click()

# time.sleep(5)
driver.implicitly_wait(60)

# 判断价格
price = "/html/body/div[4]/div/ul/li/div/p[2]/strong"
try:
    e = driver.find_element_by_xpath(price)
    assert e.text == "￥168.00"
    print("测试用例执行通过！")
except:
    print("测试用例执行失败！")