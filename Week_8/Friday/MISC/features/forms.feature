@forms
Feature: Form Interactions
  As a user
  I want to interact with various form elements
  So that I can complete different tasks

  @checkboxes
  Scenario: Toggle checkboxes
    Given the user is on the checkboxes page
    When the user checks all checkboxes
    Then all checkboxes should be checked
    When the user unchecks all checkboxes
    Then all checkboxes should be unchecked

  @dropdown
  Scenario Outline: Select dropdown options
    Given the user is on the dropdown page
    When the user selects "<option>" from the dropdown
    Then the dropdown should show "<option>" selected

    Examples:
      | option   |
      | Option 1 |
      | Option 2 |

@input
Scenario: Clear and type in input field
  Given the user is on the input page
  When the user clears the input field
  And the user types "Hello World" into the input field
  Then the input field should contain "Hello World"

@upload
Scenario: Upload a file
  Given the user is on the file upload page
  When the user uploads the file "testfile.txt"
  Then the file upload should be successful
