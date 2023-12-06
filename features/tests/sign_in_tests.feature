Feature: Verify Sign in Page opened

#  Scenario: Logged out user can sign in
#    Given Open target
#    When Click Sign In
#    And Click sign in navigation menu
#    Then Verify Sign in page opened

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original windows
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original


  Scenario: After entering incorrect login error shows
    Given Open sign in page
    When Enter incorrect email and password combination
    And Click login button
    Then Verify 'We can't find your account.' message is shown