Feature: Check Product Availability on Crayola

Background: Navigate to Crayola main page
    Given Open crayola main page

Scenario: Verify products show their availability status
    When Navigate to the Crayola product page
    And Select a product
    Then Verify product availability status is displayed