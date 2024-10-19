import time

import allure
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.ContactsPage import Contact
from pages.ShopPage import Shop
from pages.CartsPage import Cart

@allure.severity(allure.severity_level.CRITICAL)
def test_all_mandatory_fields(driver):
    home_page = HomePage(driver)
    contact_page = Contact(driver)

    driver.get("https://jupiter.cloud.planittesting.com/#/")
    # navigating to contact page
    home_page.navigate_to_contact_page();
    # clicking on submit button
    contact_page.click_submit_button();
    # capturing the error header from the header message.
    error_message = contact_page.get_message_from_header()
    assert error_message == "We welcome your feedback - but we won't get it unless you complete the form correctly."
    # capturing error message from the text box forename
    fore_name_error_message = contact_page.validate_forename_error_when_blank()
    assert fore_name_error_message == "Forename is required"
    # capturing error message from the text box email
    email_name_error_message = contact_page.validate_email_error_when_blank()
    assert email_name_error_message == "Email is required"
    # capturing error message from the text box blank message
    message_name_error_message = contact_page.validate_message_error_when_blank()
    assert message_name_error_message == "Message is required"

    # Entering the forename field
    contact_page.set_forename("FOO")
    # Entering the Email field
    contact_page.set_email("foo@bar.com")
    # Entering the Message field
    contact_page.set_message("Today is a sunny Day.")
    header_text_after_entering_fields = contact_page.get_message_from_header()
    assert header_text_after_entering_fields == "We welcome your feedback - tell it how it is."
    driver.quit()

@allure.severity(allure.severity_level.NORMAL)
def test_fill_contact_form_read_success_message(driver):
    home_page = HomePage(driver)
    contact_page = Contact(driver)
    driver.get("https://jupiter.cloud.planittesting.com/#/")
    # navigating to contact page
    home_page.navigate_to_contact_page();
    # Entering the forename field
    contact_page.set_forename("foo")
    # Entering the Email field
    contact_page.set_email("foo@bar.com")
    # Entering the Message field
    contact_page.set_message("Today is a sunny Day.")
    # clicking on submit button
    contact_page.click_submit_button();
    time.sleep(10)
    # verifying the success message after for is complete
    header_text_after_entering_fields = contact_page.get_message_from_header()
    assert header_text_after_entering_fields == "Thanks foo, we appreciate your feedback."
    driver.quit()

@allure.severity(allure.severity_level.CRITICAL)
def test_add_products_in_cart(driver):
    driver.get("https://jupiter.cloud.planittesting.com/#/")
    shop = Shop(driver)
    home_page = HomePage(driver)
    cart_page = Cart(driver)

    #Adding two Stuffed Frog
    home_page.navigate_to_shop_page()
    shop.buy_product("Stuffed Frog")
    shop.buy_product("Stuffed Frog")
    # Adding two Fluffy Bunny
    shop.buy_product("Fluffy Bunny")
    shop.buy_product("Fluffy Bunny")
    shop.buy_product("Fluffy Bunny")
    shop.buy_product("Fluffy Bunny")
    shop.buy_product("Fluffy Bunny")
    # Adding two Valentine Bear
    shop.buy_product("Valentine Bear")
    shop.buy_product("Valentine Bear")
    shop.buy_product("Valentine Bear")

    #navigating to cart page
    shop.navigate_to_cart_page()

    # Verify that total = sum(sub totals)
    cart_page.validate_total_price_is_correct()

    #verify price of each product
    home_page.navigate_to_shop_page()
    price_from_shop_page = shop.get_price_of_product_from_shop("Stuffed Frog")
    time.sleep(2)
    home_page.navigate_to_cart_page()
    price_from_cart_page = cart_page.get_price_of_product_from_cart("Stuffed Frog")
    assert price_from_shop_page == price_from_cart_page

    # Verify the subtotal for each product is correct
    subtotal_from_cart = cart_page.get_subtotal_of_product("Stuffed Frog")
    quantity_from_cart = cart_page.get_quantity_of_product_from_cart("Stuffed Frog")
    home_page.navigate_to_shop_page()
    price_from_shop_page = shop.get_price_of_product_from_shop("Stuffed Frog")
    assert float(subtotal_from_cart) == quantity_from_cart * float(price_from_shop_page)
    driver.quit()

