import time

from behave import *

@given('I insert username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page_object.insert_username(username)
    context.login_page_object.insert_password(password)

@given('I click the login button')
def step_impl(context):
    context.login_page_object.click_login_button()

@given('I can login into the application and see the list of products')
def step_impl(context):
    context.inventory_page_object.check_current_url()

@given('I can proceed to shopping cart page')
def step_impl(context):
    context.shopping_cart_page_object.navigate_to_shopping_cart_page()

# @when('I add item to the cart')
# def step_impl(context):
#     context.shopping_cart_page_object.click_checkout_button()
#
# @then('the item should be displayed in the cart')
# def step_impl(context):
#     context.checkout_object.check_checkout_url()

@when('I click on the checkout button')
def step_impl(context):
    context.shopping_cart_page_object.click_checkout_button()

@when('I click on the continue shopping button')
def step_impl(context):
        context.shopping_cart_page_object.click_continue_shopping_button()


@then('I am redirected to a checkout page')
def step_impl(context):
    context.checkout_page_object.check_checkout_url()

@then('I am redirected to the inventory page')
def step_impl(context):
    context.inventory_page_object.check_current_url()



