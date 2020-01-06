from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator, timeout=10):
    """
        参数：
            driver：浏览器句柄
            locator: 元素定位方法("id", "xxx")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"

            timeout: 超时时间, 默认10


        返回值：元素本身
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))