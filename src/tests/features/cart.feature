Feature: Shopping cart price calculations
  As a customer
  I want to verify the prices and totals in my cart
  So that I can ensure my order is calculated correctly

  @cart @regression
  Scenario: Verify product subtotal calculation
    Given I navigate to the home page
    When I navigate to the "Shop" page
    And I add "2" pieces of "Stuffed Frog" to my cart
    And I add "5" pieces of "Fluffy Bunny" to my cart
    And I add "3" pieces of "Valentine Bear" to my cart
    When I navigate to the "Cart" page
    Then I should see that the subtotal for each product is calculated correctly
    And I should see that the price for each product is correct
    And I should see that the sum is the total of all subtotals of the products in the cart
