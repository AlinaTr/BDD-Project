import time

from behave import *


@when('I click on the add to cart "{product_name}" button on the inventory page')
def step_impl(context, product_name):
    context.inventory_page_object.add_product_to_cart(product_name)


@when('I click on the remove button "{product_name}" on the on the inventory page')
def step_impl(context,product_name):
    context.inventory_page_object.remove_product_from_cart(product_name)

@then('the product should be added to cart')
def step_impl(context):
    assert context.inventory_page_object.is_product_added_to_cart()

@then('the product should be removed from the cart')
def step_impl(context):
    assert context.inventory_page_object.is_product_removed_from_cart()