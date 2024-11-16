Feature: Navigate to the "Test Automation in the Real World" book

  Scenario: Access the website and click on "Test Automation in the Real World" book
    Given I am on the "https://automationbookstore.dev" page
    When I click on the "Test Automation in the Real World" book
    Then I should see the book details page
    And the result should be saved in a test result file
