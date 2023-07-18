from base_page import BasePage



class Checkout(BasePage):

    def check_checkout_url(self):
        expected_url = 'https://www.saucedemo.com/checkout-step-one.html'
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, "error: Invalid URL"
