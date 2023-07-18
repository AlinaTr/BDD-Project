from base_page import BasePage
from selenium.webdriver.common.by import By

class ShoppingCart(BasePage):


    def navigate_to_shopping_cart_page(self):
        self.chrome.get('https://www.saucedemo.com/cart.html')

    def click_checkout_button(self):
        self.chrome.find_element(By.ID, 'checkout').click()


