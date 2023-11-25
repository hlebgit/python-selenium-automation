# Created by hleb at 11/21/23
Feature: Verify colors of the product
  # Enter feature description here

  #EX 2
  Scenario: Verify colors
    Given Open target page with product 'Sweater'
    Then Verify user can click through colors

  #EX 3
  Scenario: Verify Target search results
    Given Open target
    When Search for Juice
    Then Verify product name and image