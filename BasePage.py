from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 20)
        self._action = ActionChains(self._driver)

    def find_element(self, locator):
        return self._driver.find_element(*locator)

    def find_elements(self, locator):
        return self._driver.find_elements(*locator)