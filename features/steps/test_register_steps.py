# features/steps/test_register_steps.py:

from behave import given, when, then
from fastapi.testclient import TestClient
from app.fastapi_app import app


@given('the FastAPI application is running')
def step_given_application_running(context):
    context.client = TestClient(app)


@when('a profile with the name "{full_name}" is registered')
def step_when_register_profile(context, full_name):
    response = context.client.post("/register", json={"fullName": full_name})
    context.response = response


@then('the response status code should be {status_code:d}')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == status_code


@then('the response text should contain "{expected_text}"')
def step_then_check_response_text(context, expected_text):
    assert expected_text in context.response.text
