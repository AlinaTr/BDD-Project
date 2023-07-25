from base_page import BasePage
from selenium.webdriver.common.by import By

class ShoppingCart(BasePage):


    def navigate_to_shopping_cart_page(self):
        self.chrome.get('https://www.saucedemo.com/cart.html')

    def click_checkout_button(self):
        self.chrome.find_element(By.ID, 'checkout').click()

    def click_continue_shopping_button(self):
        self.chrome.find_element(By.ID, 'continue-shopping').click()

    def check_current_url(self):
        expected = "https://www.saucedemo.com/cart.html"
        actual = self.chrome.current_url
        assert expected == actual, "Error: invlid url"





