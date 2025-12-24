"""
Waiting strategy tests for dynamic content.

Targets:
- https://the-internet.herokuapp.com/dynamic_loading/1
- https://the-internet.herokuapp.com/dynamic_loading/2
- https://the-internet.herokuapp.com/dynamic_controls
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # Note: We're NOT setting implicit wait here to practice explicit waits
    yield driver
    driver.quit()


class TestExplicitWaits:
    """Test explicit waiting strategies."""

    def test_wait_for_element_visibility(self, driver):
        """
        Wait for hidden element to become visible.

        Page: dynamic_loading/1 - Element is hidden initially
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        # Click Start button
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # Wait for hidden element to become visible
        wait = WebDriverWait(driver, 10)
        hello_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        assert hello_text.text == "Hello World!"

    def test_wait_for_element_presence(self, driver):
        """
        Wait for element to appear in DOM.

        Page: dynamic_loading/2 - Element is added to DOM after loading
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # Click Start button
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # TODO: Wait for element to be present in DOM
        # Then wait for it to be visible

        # YOUR CODE HERE
        pass

    def test_wait_for_element_clickable(self, driver):
        """
        Wait for element to become clickable.

        Page: dynamic_controls - Enable/disable input
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")

        # The input is initially disabled
        text_input = driver.find_element(By.CSS_SELECTOR, "#input-example input")
        assert not text_input.is_enabled()

        # Click Enable button
        enable_btn = driver.find_element(By.CSS_SELECTOR, "#input-example button")
        enable_btn.click()

        # TODO: Wait for input to become enabled/clickable
        # Then type into it

        # YOUR CODE HERE
        pass

    def test_wait_for_text_in_element(self, driver):
        """
        Wait for specific text to appear in an element.
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")

        # Click Remove button for checkbox
        remove_btn = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
        remove_btn.click()

        # TODO: Wait for message "It's gone!" to appear

        # YOUR CODE HERE
        pass

    def test_wait_for_staleness(self, driver):
        """
        Wait for element to become stale (removed from DOM).
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")

        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")

        # Click Remove
        remove_btn = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
        remove_btn.click()

        # TODO: Wait for checkbox to become stale
        # Use EC.staleness_of(checkbox)

        # YOUR CODE HERE
        pass


class TestCustomWaits:
    """Create custom wait conditions."""

    def test_custom_wait_condition(self, driver):
        """
        Implement a custom wait condition.
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        # Custom condition: Wait for loading spinner to disappear
        def loading_complete(driver):
            try:
                loading = driver.find_element(By.ID, "loading")
                return not loading.is_displayed()
            except:
                return True

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(loading_complete)

        # Now check the result
        result = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        assert result.is_displayed()

    def test_custom_wait_with_lambda(self, driver):
        """
        Use lambda for simple custom conditions.
        """
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # TODO: Use lambda for custom condition
        # Example: wait.until(lambda d: "Hello" in d.page_source)

        # YOUR CODE HERE
        pass