Feature: Contact form validation and submission
  As a user
  I want to submit the contact form
  So that I can send feedback successfully

  Background:
    Given I navigate to the home page
    When I navigate to the "Contact" page

  @validation @TC-01
  Scenario: Display validation errors when submitting an empty feedback form
    When I click the "Submit" button
    Then I should see that mandatory field error messages should be displayed
    When I populate all mandatory feedback form fields
    And I click the "Submit" button
    Then I should see the my feedback has been submitted successfully

  @smoke @regression @repeat_5 @TC-02
  Scenario: Submit a feedback form with filled out Mandatory Fields
    When I populate all mandatory feedback form fields
    And I click the "Submit" button
    Then I should see the my feedback has been submitted successfully

  @smoke @regression
  Scenario: Submit a feedback form with all fields filled out
    When I populate all feedback form fields
    And I click the "Submit" button
    Then I should see the my feedback has been submitted successfully
