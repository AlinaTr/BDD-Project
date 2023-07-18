import time

from selenium.common import NoSuchElementException

from base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):

    PRODUCTS = {
        'backpack': 'sauce-labs-backpack',
        'tshirt' : 'sauce-labs-bolt-t-shirt',
        'bike_light' : 'sauce-labs-bike-light',
        'jacket' : 'sauce-labs-fleece-jacket',
        'onesie' : 'sauce-labs-onesie',
        'tshirt_red' : 'test.allthethings()-t-shirt-(red)'
    }

    # def navigate_to_inventory_page(self):
    #     self.chrome.get('https://www.saucedemo.com/inventory.html')

    def check_current_url(self):
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, "Error: Invalid URL"

    def add_product_to_cart(self,product_name):
        # self.chrome.find_element(By.XPATH, product_xpath).click()

        # xpath_el = '//*[@id="add-to-cart-'  + product_id + '"]'
        # self.chrome.find_element(By.XPATH, xpath_el).click()

        product_id = self.PRODUCTS.get(product_name)
        if product_id:
            xpath = '//*[@id="add-to-cart-' + product_id + '"]'
            add_to_cart_button=self.chrome.find_element(By.XPATH, xpath)
            add_to_cart_button.click()
        else:
            print(f'Product {product_name} not found.')



    # add_product_to_cart()
    # add_product_to_cart()

    def remove_product_from_cart(self, product_name):

        product_id = self.PRODUCTS.get(product_name)
        if product_id:
            xpath = '//*[@id="add-to-cart-' + product_id + '"]'
            remove_button = self.chrome.find_element(By.XPATH, xpath)
            remove_button.click()
        else:
            print(f'Product {product_name} not found.')

    def is_product_added_to_cart(self):
        cart = self.chrome.find_element(By.XPATH, '//*[@class="shopping_cart_badge"]')
        return cart.text != ''

#Option 2:

        # try:
        #     cart = self.chrome.find_element(By.XPATH, '//*[@class="shopping_cart_badge"]')
        #     return cart.text != ''
        # except NoSuchElementException:
        #     return False
    #
    def is_product_removed_from_cart(self):
        cart = self.chrome.find_element(By.XPATH, '//*[@class="shopping_cart_badge"]')
        return cart.text != ''