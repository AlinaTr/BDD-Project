from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    # //*[@id="password"]
    USERNAME = (By.ID, 'user-name') # *USERNAME <-> *(By.ID, 'user-name') -> By.ID, 'user-name'
    PASSWORD = (By.ID, 'password')
    BUTTON = (By.ID, 'login-button')
    ERROR = (By.XPATH, '//h3[@data-test="error"]')

    def navigate_to_login_page(self):
        self.chrome.get("https://www.saucedemo.com")

    def insert_username(self, username):
        self.chrome.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.chrome.find_element(*self.BUTTON).click()

    def check_login_error_message(self, error_message):
        self.check_error_message(self.ERROR, error_message)


