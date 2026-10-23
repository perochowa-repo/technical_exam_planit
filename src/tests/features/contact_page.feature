Feature: Contact form validation and submission
  As a user
  I want to submit the contact form
  So that I can send a message successfully

  Background:
    Given I am on the home page
    When I navigate to the contact page

  @validation
  Scenario: Display validation errors when submitting an empty contact form
    When I click the submit button
    Then the mandatory field error messages should be displayed
    When I populate all mandatory contact fields
    Then the validation error messages should no longer be displayed

  @smoke @regression @repeat_5
  Scenario: Submit the contact form successfully
    When I populate all mandatory contact fields
    And I click the submit button
    Then a successful submission message should be displayed
