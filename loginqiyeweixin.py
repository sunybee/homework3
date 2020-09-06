from selenium import webdriver
from selenium.webdriver.chrome.options import Option

import pytest

class Testlogin():
    def setup_method(self,method):
        option = Option()
        option.debugger_address ="localhost:9222"
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()
    def test_contract(self):
        self.driver.find_element(By.ID,jstree-marker)