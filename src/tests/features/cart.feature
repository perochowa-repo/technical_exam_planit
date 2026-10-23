Feature: Shopping cart price calculations
  As a customer
  I want to verify the prices and totals in my cart
  So that I can ensure my order is calculated correctly

  Background:
    Given I am on the home page

  @cart @regression
  Scenario Outline: Verify product subtotal calculation
    Given I have <quantity> "<product>" in my cart
    When I navigate to the cart page
    Then the unit price should be <unit_price>
    And the subtotal should be <subtotal>

    Examples:
      | product        | quantity | unit_price | subtotal |
      | Stuffed Frog   | 2        | 10.99      | 21.98    |
      | Fluffy Bunny   | 5        | 9.99       | 49.95    |
      | Valentine Bear | 3        | 14.99      | 44.97    |
