# from behave import *
#
# @given('I am on the saucedemo inventory page')
# def step_impl(context):
#     context.inventory_page_object.navigate_to_inventory_page()
#
# @when('I click on the add to cart button')
# def step_impl(context):
#     context.inventory_page_object.add_product_to_cart()
#
# @when('I click on the remove button')
# def step_impl(context):
#     context.inventory_page_object.remove_product_from_cart()
#
# @then('The product should be added to the cart')
# def step_impl(context):
#     assert context.inventory_page_object.is_product_added_to_cart()
#
# @then('The product should be removed from the cart')
# def step_impl(context):
#     assert context.inventory_page_object.is_product_removed_from_cart()