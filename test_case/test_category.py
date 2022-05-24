from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from page.commoditymanagement.main import Main


class TestCateGory:
    def setup(self):
        self.main = Main()

    def test_category_add(self):
        # self._driver = webdriver.Chrome()
        # _base_url = 'http://192.168.50.23:8380'
        # self._driver.get(_base_url)
        # self._driver.find_element(By.ID,'username').send_keys('admin')
        # self._driver.find_element(By.ID, 'password').send_keys('admin')
        # self._driver.find_element(By.ID, 'scode').send_keys(1234)
        # self._driver.find_element(By.ID, 'submit').click()
        # asd = self._driver.get_cookies()
        # print(asd)

        self.main.category.category_add()
