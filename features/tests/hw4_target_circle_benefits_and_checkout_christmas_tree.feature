# Created by hleb at 11/14/23
Feature: Verify Target Circle Benefits and User can add and check out product

  #EX
  Scenario: User can see 5 benefits of Target Circle
    Given Open target circle page
    Then Verify user can see 5 benefits


    #EX
  Scenario: Verify product in the cart
    Given Open product page
    When Add product to the cart
    And Check out
    Then Verify title

