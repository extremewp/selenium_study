from selenium import webdriver
from selenium.webdriver.common.by import By

from page.commoditymanagement.category import CateGory


class Main:
    def __init__(self):
        self._driver = webdriver.Chrome()
        cookies = [
            {'domain': '192.168.50.23', 'httpOnly': False, 'name': 'cityTitle', 'path': '/', 'secure': False,
             'value': ''}, {'domain': '192.168.50.23', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/',
                            'secure': False, 'value': '1C188421BFE32790455547519CFE7645'}]
        self._driver.get('http://192.168.50.23:8380')
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get('http://192.168.50.23:8380')
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    @property
    def category(self):
        self._driver.find_element(By.XPATH,'/html/body/div[2]/ul/li[2]/a').click()
        self._driver.find_element(By.ID,'menu_jzz-cat').click()
        return CateGory(self._driver)
