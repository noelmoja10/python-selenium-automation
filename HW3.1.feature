# Created by noelcanlas at 10/9/22
Feature: Amazon Cart Icon Empty
  # This shows that there's no item in the cart

  Scenario: Cart is empty
    Given Open Amazon page
    When Click the Cart Icon on top right
    Then Verify if Cart icon is clickable
    Then Verify if cart is empty
