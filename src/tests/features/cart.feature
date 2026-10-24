Feature: Shopping cart price calculations
  As a customer
  I want to verify the prices and totals in my cart
  So that I can ensure my order is calculated correctly

  Background:
    Given I navigate to the home page
    When I navigate to the "Shop" page

  @cart @regression
  Scenario Outline: Verify product subtotal calculation
    Given I add <quantity> "<product>" to my cart
    When I navigate to the cart page
    Then I should see that that the subtotal for each product is calculated correctly
    And I should see that the price for each product is calculated correctly
    And I should see that the sum is the total of all subtotals of the products in the cart

    Examples:
      | product        | quantity |
      | Stuffed Frog   | 2        |
      | Fluffy Bunny   | 5        |
      | Valentine Bear | 3        |
