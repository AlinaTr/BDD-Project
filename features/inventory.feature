Feature: Check the functionality of the Inventory Page

  Background:
    Given I am on the saucedemo login page
    And I insert username "standard_user" and password "secret_sauce"
    And I click the login button
    And I can login into the application and see the list of products
#
#    # Scenariu 1: I can add to cart items
#    # Scenariu 2: I can remove items from cart


@add-products
   Scenario Outline: Check that I can add multiple products to cart page
    When I click on the add to cart "<product_name>" button on the inventory page
    Then the product should be added to cart
  Examples:
  | product_name |
  | backpack |
  | sauce_labs_tshirt   |
  | sauce_labs_bike_light |
  |  sauce_labs_fleece_jacket         |
  |  sauce_labs_onesie                |
  | long_sleeve_tshirt                |

@add-products
  Scenario Outline: Check that I can add one product to cart page
  When I click on the add to cart "<product_name>" button on the inventory page
  Then the product should be added to cart
  Examples:
   | product_name |
  | sauce-labs-backpack |


@remove-products
Scenario Outline: Check that I can remove multiple products from cart
  When I click on the remove button "<product_name>" on the on the inventory page
  Then the product should be removed from the cart
  Examples:
  | product_name |
  | sauce-labs-backpack |
  | sauce_labs_tshirt   |
  | sauce_labs_bike_light |
  |  sauce_labs_fleece_jacket         |
  |  sauce_labs_onesie                |
  | long_sleeve_tshirt                |

@remove-products
Scenario Outline: Check that I can remove one product from cart page
  When I click on the remove button "<product_name>" on the on the inventory page
  Then the product should be removed from the cart
  Examples:
  | product_name |
  | sauce_labs_tshirt |
