"""
Authentication Step Definitions - implement together
"""
from behave import given, when, then

from pages.login_page import LoginPage


@given('the user is on the login page')
def step_on_login_page(context):
    """Navigate to login page."""
    # TODO: Implement using context.login_page
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()

@given('the user is logged in as "{username}"')
def step_logged_in_as(context, username):
    """Log in as specified user."""
    # TODO: Implement
    # Navigate to login, enter credentials, verify success
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()
    context.login_page.login(username, "SuperSecretPassword!")
    assert context.login_page.is_login_successful(), f"Login failed for user {username}"

@when('the user enters username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('the user enters password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when('the user clicks the login button')
def step_click_login(context):
    context.login_page.click_login()

@when('the user clicks the logout button')
def step_click_logout(context):
    context.login_page.click_logout()

@then('the user should be logged in successfully')
def step_logged_in_successfully(context):
    assert context.login_page.is_login_successful(), "User was not logged in successfully"

@then('the user should see welcome message "{message}"')
def step_see_welcome_message(context, message):
    flash_message = context.login_page.get_flash_message()
    assert message in flash_message, f'Expected welcome message "{message}", but got "{flash_message}"'

@then('the user should be logged out')
def step_logged_out(context):
    # You can check URL or flash message to verify logout
    assert "/login" in context.driver.current_url or "logged out" in context.login_page.get_flash_message().lower()

@then('the user should see message "{message}"')
def step_see_message(context, message):
    flash_message = context.login_page.get_flash_message()
    assert message in flash_message, f'Expected message "{message}", but got "{flash_message}"'

@then('the login result should be "{result}"')
def step_login_result(context, result):
    if result == "success":
        assert context.login_page.is_login_successful(), "Expected login success, but login failed"
    else:
        assert not context.login_page.is_login_successful(), "Expected login failure, but login succeeded"