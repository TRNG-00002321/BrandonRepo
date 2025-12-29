@cart
Feature: Shopping Cart Management
  As an online shopper
  I want to manage items in my shopping cart
  So that I can purchase the products I need

  Background:
    Given the user is logged in
    And the product catalog is available

  @smoke
  Scenario: Add single item to cart
    # TODO: Write the scenario
    Given the user is on a product page
    When the user clicks add to cart
    Then the item will appear in the cart
    And the cart count updates


  Scenario: Add multiple quantities of an item
    Given the user is on a product page
    And the quantity is set to 3
    When the user clicks add to cart
    Then 3 items will appear in the cart
    And the cart count updates to 3

  Scenario: View cart contents
    Given the user is on a product page
    And the user has added an item to the cart
    When the user clicks on the cart icon
    Then the cart contents are displayed
    And the item details are shown

  Scenario: Update item quantity in cart
    Given the user is on the cart details page
    And the user has 3 items in the cart
    And the total price displays "$3.00"
    When the user decreases the quantity of the item by 1
    Then the cart is updated to 2 items
    And the total price displays "$2.00"


  Scenario: Remove item from cart
    Given the user is on the cart details page
    And the user has 1 item in the cart
    When the user removes 1 item from the cart
    Then the cart is empty
    And the total price displays "$0.00"


  Scenario: Empty cart displays message
    Given the user is on the home page
    And the cart is empty
    When the user clicks on the cart icon
    Then the user is redirected to the cart details page
    And the page displays a message indicating the cart is empty


  Scenario: Cart total calculates correctly
    Given the user has the following items in cart:
      | Product     | Price  | Quantity |
      | Widget A    | 10.00  | 2        |
      | Widget B    | 25.00  | 1        |
    Then the cart subtotal should be "$45.00"