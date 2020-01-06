#1. 导入selenium
import time
from selenium import webdriver

#2. 实例化浏览器并且获得浏览器句柄（打开浏览器并且获得浏览器的操作对象）
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
#3. 打开百度的网址
driver.get("https://www.baidu.com/")
#4. 在输入框输入iphone12 

# id定位
# e = driver.find_element_by_id("kw")
# e.send_keys("iphone12")
# #5. 点击百度一下按钮
# e1 = driver.find_element_by_id("su")
# e1.click()

#2. xpath定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("iphone12")

# 3. name定位
# driver.find_element_by_name('wd').send_keys("iphone12")

# 4. classname
# driver.find_element_by_class_name('s_ipt').send_keys("iphone12")

# 5. css selector
driver.find_element_by_css_selector('#kw').send_keys("iphone12")
driver.find_element_by_xpath('//*[@id="su"]').click()

# 6. link_text 只能用于超链接 a标签
# driver.find_element_by_link_text("新闻").click()

# 7. partial_link_text 只能用于超链接 a标签
# driver.find_element_by_partial_link_text("hao").click()

# 8. tag_name
# driver.find_element_by_tag_name("div")

#6. 检查搜索结果
#调用变量，获取网页的标题
# 断言通过，测试执行通过；断言失败，断言就会报错，测试执行失败！
time.sleep(5)
a = driver.title
print(a)
assert a == "iphone12_百度搜索"
print("测试用例执行通过！")

driver.quit()