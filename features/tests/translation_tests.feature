Feature: Translation for Crayola

Background: Navigate to Crayola main page
    Given Open crayola main page

Scenario Outline: Verify site text translates to selected language
    When Select language <language>
    Then Verify text is translated to <language>
    Examples:
    |language                |
    |Spanish (Mexico)        |
    |Italian (Italy)         |
    |English (United Kingdom)|
    |English (Australia)     |
