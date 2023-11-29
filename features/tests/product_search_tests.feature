Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: Target User can search and add a product to cart
    Given Open Target
    When Search for Sweater
    And Add first product of the search results to the cart
    And Checkout
    Then Verify Cart has 1 Item