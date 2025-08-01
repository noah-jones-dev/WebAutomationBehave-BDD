Feature: Search Products on Crayola

Background: Navigate to Crayola main page
    Given Open crayola main page

Scenario Outline: Verify products can be searched and selected.
    When Crayola search for <product>
    Then Displays search results for <product>
    When Select a <product> from the search results
    Then Verify <product> detail displays
    Examples:
    |product        |
    |Coffee         |
    |Crayons        |
    |Markers        |
    |Paints         |
