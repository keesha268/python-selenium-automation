# Created by keesh at 3/08/2023
Feature: Amazon search tests

  Scenario: User user sees Sign In when clicking on orders
    Given Open Amazon page
    When Click on orders button
    Then Verify that text "Sign in" are shown