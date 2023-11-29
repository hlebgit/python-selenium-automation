Feature: Verify Sign in Page opened

  Scenario: Logged out user can sign in
    Given Open target
    When Click Sign In
    And Click sign in navigation menu
    Then Verify Sign in page opened