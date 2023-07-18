from base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):

    # def navigate_to_inventory_page(self):
    #     self.chrome.get('https://www.saucedemo.com/inventory.html')

    def check_current_url(self):
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, "Error: Invalid URL"

    # def add_product_to_cart(self):
    #     self.chrome.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    #
    # def remove_product_from_cart(self):
    #     self.chrome.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    #
    # def is_product_added_to_cart(self):
    #     cart = self.chrome.find_element(By.XPATH, '//*[@class="shopping_cart_badge"]')
    #     return cart.text == '1'
    #
    # def is_product_removed_from_cart(self):
    #     cart = self.chrome.find_element(By.XPATH, '//*[@class="shopping_cart_badge"]')
    #     return cart.text == ''