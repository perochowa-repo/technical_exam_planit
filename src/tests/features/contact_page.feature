Feature: Contact form validation and submission
  As a user
  I want to submit the contact form
  So that I can send a message successfully

  Background:
    Given I navigate to the home page
    When I navigate to the "Contact" page

  @validation
  Scenario: Display validation errors when submitting an empty contact form
    When I click the "Submit" button
    Then I should see that mandatory field error messages should be displayed
    When I populate all mandatory contact fields
    And I click the "Submit" button
    Then I should see the my feedback has been submitted successfully

  @smoke @regression @repeat_5
  Scenario: Submit the contact form successfully
    When I populate all mandatory contact fields
    And I click the "Submit" button
    Then I should see the my feedback has been submitted successfully
