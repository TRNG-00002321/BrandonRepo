from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Locators for checkboxes page
CHECKBOXES_URL = "https://the-internet.herokuapp.com/checkboxes"
CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

# Locators for dropdown page
DROPDOWN_URL = "https://the-internet.herokuapp.com/dropdown"
DROPDOWN = (By.ID, "dropdown")

@given('the user is on the checkboxes page')
def step_on_checkboxes_page(context):
    context.driver.get(CHECKBOXES_URL)

@when('the user checks all checkboxes')
def step_check_all_checkboxes(context):
    checkboxes = context.driver.find_elements(*CHECKBOXES)
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

@when('the user unchecks all checkboxes')
def step_uncheck_all_checkboxes(context):
    checkboxes = context.driver.find_elements(*CHECKBOXES)
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()

@then('all checkboxes should be checked')
def step_all_checked(context):
    checkboxes = context.driver.find_elements(*CHECKBOXES)
    assert all(cb.is_selected() for cb in checkboxes), "Not all checkboxes are checked"

@then('all checkboxes should be unchecked')
def step_all_unchecked(context):
    checkboxes = context.driver.find_elements(*CHECKBOXES)
    assert all(not cb.is_selected() for cb in checkboxes), "Not all checkboxes are unchecked"

@given('the user is on the dropdown page')
def step_on_dropdown_page(context):
    context.driver.get(DROPDOWN_URL)

@when('the user selects "{option}" from the dropdown')
def step_select_option(context, option):
    select_element = context.driver.find_element(*DROPDOWN)
    select = Select(select_element)
    select.select_by_visible_text(option)

@then('the dropdown should show "{option}" selected')
def step_verify_selected(context, option):
    select_element = context.driver.find_element(*DROPDOWN)
    select = Select(select_element)
    selected_option = select.first_selected_option.text
    assert selected_option == option, f"Expected '{option}', but got '{selected_option}'"
