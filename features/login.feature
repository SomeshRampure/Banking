Feature: Banking Login

  Scenario: Valid login
    Given I am on the banking login page
    When I enter valid credentials
    Then I should be logged in

  Scenario: Invalid login
    Given I am on the banking login page
    When I enter invalid credentials
    Then I should see an error message
