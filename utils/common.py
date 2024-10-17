from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Utils:
    def __init__(self,driver):
        self.driver =driver;
        self.wait = WebDriverWait(self.driver,10)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))


