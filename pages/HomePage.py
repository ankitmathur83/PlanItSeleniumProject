from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
class HomePage(BasePage):
    contact_link = (By.LINK_TEXT, 'Contact')
    shop_link = (By.LINK_TEXT,'Shop')
    cart_link = (By.PARTIAL_LINK_TEXT,'Cart')

    @allure.step("Navigating to the contact page")
    def navigate_to_contact_page(self):
        """navigate to contact page
        """
        self.find_element(self.contact_link).click();

    @allure.step("Navigating to the shop page")
    def navigate_to_shop_page(self):
        """navigate to the shopping page.
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.shop_link))
        self.find_element(self.shop_link).click();

    @allure.step("Navigating to the Cart Page")
    def navigate_to_cart_page(self):
        """navigate to cart page.
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.cart_link))
        self.find_element(self.cart_link).click();

