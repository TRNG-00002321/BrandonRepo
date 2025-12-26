"""
Base Page Object - implement together
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, path):
        """Navigate to a path relative to base URL."""
        # TODO: Implement together
        full_url = self.BASE_URL + path
        self.driver.get(full_url)

    def wait_for_element(self, locator):
        """Wait for element to be visible."""
        # TODO: Implement together
        self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Click on element after waiting for it."""
        # TODO: Implement together
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Type text into element after clearing it."""
        # TODO: Implement together
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from element."""
        # TODO: Implement together
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_displayed(self, locator):
        """Check if element is displayed."""
        # TODO: Implement together
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()