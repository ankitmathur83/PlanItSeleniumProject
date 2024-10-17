from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class Shop(BasePage):
    all_products_locator = (By.CLASS_NAME, "product")
    product_title = (By.CLASS_NAME, "product-title")
    cart_link = (By.XPATH,"//a[@href='#/cart']")
    product_price = (By.CLASS_NAME,"product-price")

    @allure.step("Method to click on Buy button when a product is given.")
    def buy_product(self, product_name: str):
        """Method to click on Buy button when a product is given.

        Args:
            product_name (str): product name 
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.all_products_locator))
        all_products = self.find_elements(self.all_products_locator);
        for each_product in all_products:
            if each_product.find_element(By.CLASS_NAME, "product-title").text == product_name:
                buy_button = each_product.find_element(By.CLASS_NAME, "btn")
                buy_button.click()
                break

    @allure.step("Navigate to the cart page.")
    def navigate_to_cart_page(self):
        """Navigate to the cart page
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.cart_link))
        self.find_element(self.cart_link).click();

    @allure.step("Get price from shop page given the product name.")
    def get_price_of_product_from_shop(self, product_name: str):
        """get price from shop page given the product name.

        Args:
            product_name (str): Name of Product.

        Returns:
            _type_: price of product without the $.
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.all_products_locator))
        all_products = self.find_elements(self.all_products_locator);
        for each_product in all_products:
            if each_product.find_element(By.CLASS_NAME, "product-title").text == product_name:
                product_price_shop_page = each_product.find_element(By.CLASS_NAME,"product-price").text;
                break;
        return product_price_shop_page.split("$")[1]






