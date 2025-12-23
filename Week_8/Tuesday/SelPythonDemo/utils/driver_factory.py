"""
TODO: Implement a driver factory that:
1. Uses webdriver-manager for automatic driver management
2. Provides a context manager for safe browser cleanup
3. Supports headless mode via parameter
"""

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        yield driver
    finally:
        driver.quit()