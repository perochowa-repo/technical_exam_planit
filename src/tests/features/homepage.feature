Feature: Jupiter Toys

  @homepage
  Scenario: Verify the homepage title
    Given I navigate to the homepage
    Then I should see that the page title contains "Jupiter Toys"
