"""
Test navigation functionality using Python Selenium.

Implement tests that:
1. Navigate to https://the-internet.herokuapp.com/
2. Click on "Form Authentication" link
3. Verify URL changed to /login
4. Use back/forward navigation
5. Capture screenshots at key points
"""
import pytest
from selenium.webdriver.common.by import By
import sys

sys.path.insert(0, '..')
from utils.driver_factory import driver

class TestBasics:

    #/login

    def test_navigate_to_login_page(self, driver):
        """
        Test: Navigate from home to login page

        Steps:
        1. Go to the-internet homepage
        2. Find and click "Form Authentication" link
        3. Assert URL contains "/login"
        4. Assert page contains "Login Page" heading
        """
        # YOUR CODE HERE

        #1
        driver.get("https://the-internet.herokuapp.com/")

        #2
        driver.find_element(By.LINK_TEXT, "Form Authentication").click()

        #3
        assert "/login" in driver.current_url

        #4
        element = driver.find_element(By.XPATH, "//h2[normalize-space()='Login Page']")
        assert "Login Page" in element.text



    def test_back_forward_navigation(self, driver):
        """
        Test: Browser navigation (back/forward)

        Steps:
        1. Navigate to homepage
        2. Click a link to go to another page
        3. Use driver.back() to return
        4. Assert you're on homepage
        5. Use driver.forward() to go forward
        6. Assert you're on the second page again
        """
        # YOUR CODE HERE

        #1
        driver.get("https://the-internet.herokuapp.com/")

        #2
        driver.find_element(By.LINK_TEXT, "Form Authentication").click()

        #3
        driver.back()

        #4
        assert "https://the-internet.herokuapp.com/" == driver.current_url

        #5
        driver.forward()

        #6
        assert "https://the-internet.herokuapp.com/login" == driver.current_url


    def test_capture_screenshot(self, driver):
        """
        Test: Screenshot capture

        Steps:
        1. Navigate to any page
        2. Take a full page screenshot
        3. Save it to screenshots/homepage.png
        """
        # YOUR CODE HERE

        #1
        driver.get("https://the-internet.herokuapp.com/")

        #2
        driver.find_element(By.LINK_TEXT, "Form Authentication").click()

        #3
        driver.save_screenshot("screenshots/homepage.png")


    def test_page_title(self, driver):
        """Verify the page title matches expected value."""
        # YOUR CODE HERE

        driver.get("https://the-internet.herokuapp.com/")
        element = driver.find_element(By.XPATH, "//h1[@class='heading']")

        assert "Welcome to the-internet" == element.text



    @pytest.mark.skip(reason="This is a repeat")
    def test_heading_text(self, driver):
        """Verify the main heading contains expected text."""
        # YOUR CODE HERE
        driver.get("https://the-internet.herokuapp.com/")
        element = driver.find_element(By.XPATH, "//h1[@class='heading']")



    def test_links_present(self, driver):
        """Verify that all example links are present on the page."""
        # YOUR CODE HERE
        # Use find_elements to get all links
        # Use list comprehension to extract link texts
        driver.get("https://the-internet.herokuapp.com/")
        links = driver.find_elements(By.TAG_NAME, "a")
        link_texts = [link.text for link in links]

        # Now you can assert some expected links exist, e.g.
        assert "Form Authentication" in link_texts
        assert "Dropdown" in link_texts

