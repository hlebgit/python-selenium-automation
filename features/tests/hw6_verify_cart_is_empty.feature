# Created by hleb at 11/25/23
Feature: Verify cart is empty

  Scenario: Verify Cart Is Empty Message Is Shown
    Given Open target page
    When Click on cart icon
    Then Verify Cart is Empty Message