from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _driver  = None
    _base_url = ''
    def __init__(self,driver: WebDriver = None):
        if driver == None :
            self._driver = webdriver.Chrome()
            cookies = [{'domain': '192.168.50.23', 'httpOnly': False, 'name': 'cityTitle', 'path': '/', 'secure': False, 'value': ''},
                       {'domain': '192.168.50.23', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': '64A83789384F775605A21997003ABE0B'}]
        else:
             self._driver=driver
        if self._base_url != '':
            self._driver.get(self._base_url)
            for cookie in cookies:
                self._driver.add_cookie(cookie)
            self._driver.get(self._base_url)
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()

    # 封装find_element对外提供find方法  by 是定位方法   element定位元素
    def find(self,by ,element):
        return self._driver.find_element(by,element)

    # 封装find_element对外提供find方法  by 是定位方法   element定位元素
    def finds(self,by ,element):
        return self._driver.find_elements(by,element)