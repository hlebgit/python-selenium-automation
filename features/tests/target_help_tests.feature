Feature: Search for a topic on Target Help

  Scenario: User can search for a help topic
    Given Open Target help page
    When Click Browse Help dropdown and choose Gift Cards
    Then Verify the Gift Cards page opened