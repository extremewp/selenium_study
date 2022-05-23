from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By



class CateGory:
    def __init__(self,driver:WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(10)

    def category_add(self):
        self._driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/a').click()
        self._driver.find_element(By.ID,"name").send_keys("洋酒")
        self._driver.find_element(By.ID, "sort").send_keys(6)

        self._driver.find_element(By.ID, "licenseImgUp").send_keys("D:\Develop\selenium_study\data\燕京.jpg")
#         level sort licenseImgUp  /html/body/div[3]/div/form/div[2]/table/tbody/tr/td/a[2]
        sleep(3)
        self._driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[2]/table/tbody/tr/td/a[2]").click()
        self._driver.quit()

