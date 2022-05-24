from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.commoditymanagement.base_page import BasePage


class CateGory(BasePage):

    def category_add(self):
       self.find(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/a').click()
       self.find(By.ID,"name").send_keys("洋酒")
       self.find(By.ID, "sort").send_keys(6)

       self.find(By.ID, "licenseImgUp").send_keys("D:\Develop\selenium_study\data\燕京.jpg")
#         level sort licenseImgUp  /html/body/div[3]/div/form/div[2]/table/tbody/tr/td/a[2]

       self.find(By.XPATH, "/html/body/div[3]/div/form/div[2]/table/tbody/tr/td/a[2]").click()
       sleep(3)
       self._driver.quit()

