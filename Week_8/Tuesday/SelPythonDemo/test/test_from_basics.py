"""
Basic form interaction tests.

Target: https://the-internet.herokuapp.com/login
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestLoginForm:
    """Test the login form functionality."""

    def test_successful_login(self, driver):
        """
        Test successful login with valid credentials.

        Valid credentials for this test site:
        - Username: tomsmith
        - Password: SuperSecretPassword!
        """
        driver.get("https://the-internet.herokuapp.com/login")

        # TODO: Implement login flow
        # 1. Find username field and enter "tomsmith"
        # 2. Find password field and enter "SuperSecretPassword!"
        # 3. Click the login button
        # 4. Verify success message appears
        # 5. Verify URL contains "/secure"

        # YOUR CODE HERE
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")

        login = driver.find_element(By.XPATH, "//button[@type='submit']")
        login.click()

        success_bar = driver.find_element(By.XPATH, "//div[@id='flash']")
        assert "You logged into a secure area!" in success_bar.text
        assert "/secure" in driver.current_url


    def test_failed_login_wrong_password(self, driver):
        """
        Test failed login with wrong password.

        Should display error message.
        """
        driver.get("https://the-internet.herokuapp.com/login")

        # TODO: Implement failed login
        # 1. Enter valid username, wrong password
        # 2. Click login
        # 3. Verify error message is displayed
        # 4. Verify error contains "Your password is invalid!"

        # YOUR CODE HERE
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword")

        login = driver.find_element(By.XPATH, "//button[@type='submit']")
        login.click()

        error_bar = driver.find_element(By.XPATH, "//div[@id='flash']")
        assert error_bar.is_displayed()
        assert "Your password is invalid!" in error_bar.text



    def test_clear_and_retype(self, driver):
        """
        Test clearing field and retyping.
        """
        driver.get("https://the-internet.herokuapp.com/login")

        username = driver.find_element(By.ID, "username")

        # Type, clear, retype
        username.send_keys("wrong_user")
        username.clear()
        username.send_keys("tomsmith")

        assert username.get_attribute("value") == "tomsmith"

    def test_logout_after_login(self, driver):
        """
        Test complete login and logout flow.
        """
        driver.get("https://the-internet.herokuapp.com/login")

        # TODO: Implement full login/logout cycle
        # 1. Login successfully
        # 2. Find and click logout button
        # 3. Verify redirect to login page
        # 4. Verify logout success message

        # YOUR CODE HERE
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")

        login = driver.find_element(By.XPATH, "//button[@type='submit']")
        login.click()

        success_bar = driver.find_element(By.XPATH, "//div[@id='flash']")
        assert "You logged into a secure area!" in success_bar.text
        assert "/secure" in driver.current_url

        logout = driver.find_element(By.XPATH, "//i[@class='icon-2x icon-signout']")
        logout.click()

        assert "/login" in driver.current_url

        logout_message = driver.find_element(By.XPATH, "//div[@id='flash']")
        assert "You logged out of the secure area!" in logout_message.text