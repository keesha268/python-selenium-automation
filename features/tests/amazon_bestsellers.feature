# Resubmitting HW4
Feature: Amazon bestsellers page


  Scenario: User can open the Bestsellers page
    Given Open Amazon page
    When Click on bestsellers icon
    Then Verify there are 5 links
