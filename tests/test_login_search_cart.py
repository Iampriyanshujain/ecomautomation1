import time
import json
import pytest
import os
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_path = os.path.join(project_root, "data", "user_data.json")

with open(data_path) as f:
    data = json.load(f)

login_data = data['login']
search_term = data['product']['search_term']

@pytest.mark.parametrize("credentials", login_data)
@allure.feature("Login and Search Product")
@allure.story("Valid Login and Product Cart Flow")
def test_login_search_cart(setup, credentials):
    driver = setup
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    with allure.step("Login with valid credentials"):
        login_page.enter_email(credentials["email"])
        login_page.enter_password(credentials["password"])
        login_page.click_login()
        time.sleep(3)
        assert "Logged in as" in driver.page_source, "Login failed"

    with allure.step("Search and add product to cart"):
        product_page.click_product()
        time.sleep(2)
        product_page.search_product(search_term)
        time.sleep(2)
        product_page.click_search()
        time.sleep(2)
        assert search_term.lower() in driver.page_source.lower(), "Product not found in search results"

        product_page.select_product()
        product_page.add_to_cart()
        time.sleep(2)
        product_page.close_modal()
        time.sleep(2)

    with allure.step("Verify product added and remove from cart"):
        cart_page.go_to_cart()
        time.sleep(2)
        assert "blue top" in driver.page_source.lower(), "Product not in cart"

        cart_page.delete_product()
        time.sleep(2)
        assert "Cart is empty" in driver.page_source or "Proceed To Checkout" not in driver.page_source, "Product not deleted from cart"