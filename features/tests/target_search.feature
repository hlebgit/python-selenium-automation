# Created by hleb at 11/5/23
Feature: Target

#  Scenario: Cart is empty
#    Given Open Target page
#    When Click cart icon
#    Then Empty cart message is shown

  Scenario: Logged out user can access sign in
    Given Open Target page
    When Click sign in
    And Click sign in navigation menu
    Then Verify sign in page opened