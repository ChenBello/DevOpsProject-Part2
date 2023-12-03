# pip install behave requests

# features/test_register.feature:

Feature: Test Register Profile

  Scenario: Successful registration
    Given the FastAPI application is running
    When a profile with the name "John Doe" is registered
    Then the response status code should be 200
    And the response text should contain "Successfully registered profile: John Doe"
