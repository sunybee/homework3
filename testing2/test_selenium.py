import selenium as selenium

from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
