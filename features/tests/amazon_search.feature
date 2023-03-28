# Resubmitting HW4
Feature: Amazon search tests


  Scenario: Logged out user sees Sign in page when clicking Orders
     Given Open Amazon page
     When Click Amazon Orders link
     Then Verify 'Sign in' page is opened


  Scenario: 'Your Shopping Cart is empty' shown if no product added
     Given Open Amazon page
     When Click on cart icon
     Then Verify 'Your Shopping Cart is empty.' text present


  Scenario: User can search for table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that text "table" is shown


#Scenario: User can add a product to the cart
#    Given Open Amazon page
#    When Input text Utopia Bedding Bed Pillows
#    When Click on search button
#    And Click on the first product
#    And Click on Add to cart button
#    And Open cart page
#    Then Verify cart has 1 item(s)

#  Scenario: Verify that user can see product names and images
#    Given Open Amazon page
#    When Input text coffee
#    When Click on search button
#    Then Verify that every product has a name and an image