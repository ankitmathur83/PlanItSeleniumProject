import allure
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Cart(BasePage):
    """This is a Page class for Cart functionality
    """
    all_carts_rows = (By.CSS_SELECTOR, ".cart-item")
    total_cart_value = (By.CSS_SELECTOR, ".total")
    product_quantity = (By.CLASS_NAME, ".input-mini")

    @allure.step("Get total cost from the web page")
    def _get_total_cost_cart(self):
        """_summary_
        Method internally called to get total cost from the web page
        Returns: Float value of the cost
            
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.total_cart_value))
        total_cost = self.find_element(self.total_cart_value).text
        return float(total_cost.split(": ")[1])

    @allure.step("Get sum of subtotal")
    def _get_sum_of_subtotal(self):
        """Method called internally to get sum of subtotal. 

        Returns:
            _type_: sum of  subtotals of product in cart.
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.total_cart_value))
        all_cart_items = self.find_elements(self.all_carts_rows)
        cart_value = []
        for each_item in all_cart_items:
            cell_information = each_item.find_elements(By.TAG_NAME, "td")
            for each_cell in cell_information:
                cart_value.append(each_cell.text)
        total_order_value = float(cart_value[3].lstrip('$')) + float(cart_value[8].lstrip('$')) + float(cart_value[13].lstrip('$'))
        return total_order_value

    @allure.step("Validate total price in UI and sum of subtotal is equal.")
    def validate_total_price_is_correct(self):
        """Validate total price in UI and sum of subtotal is equal.
        """
        total_cost = self._get_total_cost_cart()
        total_sub_total = self._get_sum_of_subtotal()
        assert total_cost == total_sub_total

    @allure.step("Get price of a product from the cart given the product name.")
    def get_price_of_product_from_cart(self, product_name: str):
        """get price of a product from the cart given the product name.

        Args:
            product_name (str): Name of the product for which this is to be calculated.

        Returns:
            _type_: string of cost stripping $
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.total_cart_value))
        all_cart_items = self.find_elements(self.all_carts_rows)
        for each_item in all_cart_items:
            cell_information = each_item.find_elements(By.TAG_NAME, "td")
            for i in range(len(cell_information)):
                if cell_information[0].text == product_name:
                    return cell_information[1].text.split("$")[1]
                break

    @allure.step("get subtotal of product from the carts UI given the product name.")
    def get_subtotal_of_product(self, product_name: str):
        """get subtotal of product from the carts UI given the product name.

        Args:
            product_name (str): Name of product

        Returns:
            _type_: subtotal value without the $
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.total_cart_value))
        all_cart_items = self.find_elements(self.all_carts_rows)
        for each_item in all_cart_items:
            cell_information = each_item.find_elements(By.TAG_NAME, "td")
            for i in range(len(cell_information)):
                if cell_information[0].text == product_name:
                    break
            return cell_information[3].text.split("$")[1]

    @allure.step("Get Quanity from the Cart for a given product name")
    def get_quantity_of_product_from_cart(self, product_name: str):
        """Get Quanity from the Cart for a given product name

        Args:
            product_name (str): Name of the product.

        Returns:
            _type_: Value of quantity.
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.total_cart_value))
        all_cart_items = self.find_elements(self.all_carts_rows)
        for each_item in all_cart_items:
            cell_information = each_item.find_elements(By.TAG_NAME, "td")
            for i in range(len(cell_information)):
                if cell_information[0].text == product_name:
                    return int(cell_information[2].find_element(By.NAME, "quantity").get_attribute("value"))
            break







