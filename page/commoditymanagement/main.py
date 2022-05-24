from selenium import webdriver
from selenium.webdriver.common.by import By

from page.commoditymanagement.base_page import BasePage
from page.commoditymanagement.category import CateGory


class Main(BasePage):
    _base_url = 'http://192.168.50.23:8380'
    @property
    def category(self):
        self.find(By.XPATH,'/html/body/div[2]/ul/li[2]/a').click()
        self.find(By.ID,'menu_jzz-cat').click()
        return CateGory(self._driver)
