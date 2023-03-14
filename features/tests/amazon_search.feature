# Created by keesh at 3/08/2023
Feature: Amazon search tests

#  Scenario: User can search for coffee on Amazon
#    Given Open Amazon page
#    When Input for coffee
#    When Click on search button
#    Then Verify that text "coffee" are shown

Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Utopia Bedding Bed Pillows
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)