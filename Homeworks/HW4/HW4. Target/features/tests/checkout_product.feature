# Created by hleb at 11/14/23
Feature: User can add and check out product

  Scenario: Verify product in the cart
    Given Open product page
    When Add product to the cart
    And Check out
    Then Verify title