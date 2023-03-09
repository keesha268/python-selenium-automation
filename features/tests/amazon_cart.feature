# Created by keesh at 3/08/2023
Feature: Amazon search tests

  Scenario: User can search for cart on Amazon
    Given Open Amazon page
    When Click on cart button
    Then Verify that text "Your Amazon Cart is empty" are shown