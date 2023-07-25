

from base_page import BasePage
from selenium.webdriver.common.by import By
import time


class Checkout(BasePage):

    FIRST_NAME = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME = (By.ID, 'last-name')
    POST_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CANCEL_BUTTON = (By.ID, 'cancel')

    def navigate_to_checkout_1(self):
        self.chrome.get('https://www.saucedemo.com/checkout-step-one.html')
    def check_checkout_url(self):
        expected_url = 'https://www.saucedemo.com/checkout-step-one.html'
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, "error: Invalid URL"

    def insert_first_name(self,first_name):
        self.chrome.find_element(*self.FIRST_NAME).send_keys(first_name)


    def insert_last_name(self, last_name):
        self.chrome.find_element(*self.LAST_NAME).send_keys(last_name)

    def insert_postal_code(self, post_code):
        self.chrome.find_element(*self.POST_CODE).send_keys(post_code)

    def click_continue_button(self):
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()

    def click_cancel_button(self):
        self.chrome.find_element(*self.CANCEL_BUTTON).click()

    def check_checkout_step2_url(self):
        expected_url ='https://www.saucedemo.com/checkout-step-two.html'
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, "error: Invalid URL for checkout-2"

    def check_checkout_step3_page(self):
        expected_url = 'https://www.saucedemo.com/checkout-complete.html'
        actual_url = self.chrome.current_url
        assert actual_url == expected_url, '"error: Invalid URL for checkout-3"'

    def check_overview(self):
        overview = self.chrome.find_element(By.ID, 'checkout_summary_container')
        overview.text


    def click_finish_button(self):
        self.chrome.find_element(By.ID, 'finish').click()


