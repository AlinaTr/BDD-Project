Feature: Check the functionality of Checkout page


  Background:
    Given I am on the saucedemo login page
    And I insert username "standard_user" and password "secret_sauce"
    And I click the login button
    And I can login into the application and see the list of products
    And I can proceed to shopping cart page
    And I am on the Checkout page

@checkout-step-1
    Scenario: Check that I can introduce my info and proceed to step 2
      When I introduce the first name "Jasmine", last name "Jones", postal code "022"
      And I click on continue button
      Then I am redirected to checkout step 2

@checkout-step-1
  Scenario: Check that I can return to shopping cart page from checkout page
  When I click on cancel button
  Then I am redirected to shopping cart page


  @checkout-step-2
    Scenario: Check that I have the overview of products I want to purchase and finish order
    When I am redirected to checkout step 2
    And I have an overview on the products in my cart
    And I click on finish button
    Then the order should be complete
    And I can see the confirmation message


