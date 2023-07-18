from pages.checkout_page import Checkout
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from browser import Browser
from pages.shopping_cart_page import ShoppingCart


def before_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    sau pe care vrem sa le facem disponibile inaintea TUTUROR testelor/pasilor
    """
    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.inventory_page_object = InventoryPage()
    context.shopping_cart_page_object = ShoppingCart()
    context.checkout_page_object = Checkout()


def after_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    sau pe care vrem sa le facem disponibile DUPA TOATE testele
    """
    context.browser.close()