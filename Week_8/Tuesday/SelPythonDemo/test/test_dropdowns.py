"""
Dropdown interaction tests.

Target: https://the-internet.herokuapp.com/dropdown
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://the-internet.herokuapp.com/dropdown")
    yield driver
    driver.quit()


class TestDropdowns:
    """Test dropdown interactions using Select class."""

    def test_select_by_visible_text(self, driver):
        """
        Select option by its visible text.
        """
        dropdown = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown)

        # Select "Option 1" by visible text
        select.select_by_visible_text("Option 1")

        # Verify selection
        selected = select.first_selected_option
        assert selected.text == "Option 1"

    def test_select_by_value(self, driver):
        """
        Select option by its value attribute.
        """
        # TODO: Use select_by_value("2") to select Option 2
        # Verify the selection

        # YOUR CODE HERE
        dropdown = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown)

        select.select_by_value("2")

        selected = select.first_selected_option
        assert selected.text == "Option 2"


    def test_select_by_index(self, driver):
        """
        Select option by its index (0-based).
        """
        # TODO: Use select_by_index(1) to select Option 1
        # Note: index 0 is usually the "Please select" option

        # YOUR CODE HERE

        dropdown = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown)

        select.select_by_value("1")

        selected = select.first_selected_option
        assert selected.text == "Option 1"

    def test_get_all_options(self, driver):
        """
        Get all available options from dropdown.
        """
        dropdown = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown)

        # Get all options
        all_options = select.options
        option_texts = [opt.text for opt in all_options]

        # TODO: Verify expected options are present
        # Should include "Please select an option", "Option 1", "Option 2"

        # YOUR CODE HERE
        assert "Please select an option" in option_texts
        assert "Option 1" in option_texts
        assert "Option 2" in option_texts

    def test_dropdown_without_select_class(self, driver):
        """
        Some dropdowns aren't <select> elements.
        Practice finding options through regular element interaction.
        """
        # Navigate to dropdown example with custom dropdown
        driver.get("https://the-internet.herokuapp.com/")

        # TODO: Find a different type of dropdown
        # and interact with it without Select class

        # YOUR CODE HERE
        pass