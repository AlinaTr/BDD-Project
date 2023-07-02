Feature: Check the functionality of the Login Page

  Background:
    Given I am on the saucedemo login page

  # Scenariu 1: useerr+pass corecte
  # Scenariu 2: user corect +pass incorecta
  # Scenariu 3: user incorect +pass corecta
  # Scenariu 4: user incorect +pass incorecta
  # Scenariu 5: user NONE +pass corecta
  # Scenariu 6: user NONE +pass incorecta
  # Scenariu 7: user corect +pass NONE
  # Scenariu 8: user incorect +pass NONE
  # Scenariu 9: user NONE +pass NONE
  # Scenariu 10: user blocat(locked_out) + pass corecta


  Scenario: Check that you can login into the application when providing correct credentials
    When I insert username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I can login into the application and see the list of products

  @invalid-login
  Scenario Outline: Check that you can not login into the application when providing invalid credentials
    When I insert username "<username>" and password "<password>"
    And I click the login button
    Then I cannot login into the application and I receive "<error_message>" error
  Examples:
    | username | password | error_message |
    | standard_user | incorrect_password | Epic sadface: Username and password do not match any user in this service |
    | incorrect_user | secret_sauce | Epic sadface: Username and password do not match any user in this service |
    | incorrect_user | incorrect_password | Epic sadface: Username and password do not match any user in this service |

  @invalid-login
  Scenario Outline: Check that you cannot login into the application when you don't provide both credentials
  When I do not insert username and only insert password "<password>"
  And I click the login button
  Then I cannot login into the application and I receive "<error_message>" error
  Examples:
   | password | error_message |
   | secret_sauce | Epic sadface: Username is required |
   | incorrect_password | Epic sadface: Username is required |

  @locked_out_user_login
  Scenario Outline: Check that you cannot login into the application as locked_out_user
  When I insert username "<username>" and password "<password>"
  And I click the login button
  Then I cannot login into the application and I receive "<error_message>" error
  Examples:
  | username | password | error_message |
  | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out. |
  | locked_out_user | incorrect_password | Epic sadface: Username and password do not match any user in this service |


