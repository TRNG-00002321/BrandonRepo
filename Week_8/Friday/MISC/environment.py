"""
Behave Environment Hooks - implement together
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.base_page import BasePage


def before_all(context):
    """
    Setup before all tests.
    Configure browser options, logging, etc.
    """
    # Example: Setup logging here if needed
    # import logging
    # logging.basicConfig(level=logging.INFO)
    pass


def before_scenario(context, scenario):
    """
    Setup before each scenario.
    Initialize WebDriver and page objects.
    """
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

    # Initialize page objects
    context.login_page = LoginPage(context.driver)
    context.base_page = BasePage(context.driver)


def after_scenario(context, scenario):
    """
    Cleanup after each scenario.
    Take screenshot on failure, quit browser.
    """
    if scenario.status == 'failed':
        try:
            screenshot = context.driver.get_screenshot_as_png()
            scenario.attach(screenshot, mime_type='image/png')
        except Exception as e:
            print(f"Error taking screenshot: {e}")

    if hasattr(context, 'driver'):
        context.driver.quit()


def after_all(context):
    """
    Cleanup after all tests.
    """
    # Add any final cleanup here if needed
    pass
