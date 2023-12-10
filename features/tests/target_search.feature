# Created by hleb at 11/5/23
Feature: Target

  @smoke
  Scenario: Cart is empty
    Given Open Target page
    When Click cart icon
    Then Empty cart message is shown


  @smoke
  Scenario: Logged out user can access sign in
    Given Open Target page
    When Click sign in
    And Click sign in navigation menu
    Then Verify sign in page opened