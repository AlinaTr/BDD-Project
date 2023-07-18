Feature:Check the functionality of the Shopping Cart page

  Background:
    Given I am on the saucedemo login page
    And I insert username "standard_user" and password "secret_sauce"
    And I click the login button
    And I can login into the application and see the list of products
    And I can proceed to shopping cart page


    Scenario: Check that I can proceed to Checkout
      When I click on the checkout button
      Then I am redirected to a checkout page