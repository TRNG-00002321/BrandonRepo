"""
Login Page Object - implement together
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button")

    def navigate_to_login(self):
        """Navigate to login page."""
        # TODO: Implement
        self.navigate_to("/login")

    def enter_username(self, username):
        """Enter username in the field."""
        # TODO: Implement
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password in the field."""
        # TODO: Implement
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button."""
        # TODO: Implement
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Complete login flow."""
        # TODO: Implement - combine above methods
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        """Get the flash message text."""
        # TODO: Implement
        return self.get_text(self.FLASH_MESSAGE)

    def is_login_successful(self):
        """Check if login was successful."""
        # TODO: Implement - check URL or message
        return "/secure" in self.driver.current_url

    def click_logout(self):
        """Click the logout button."""
        # TODO: Implement
        self.click(self.LOGOUT_BUTTON)