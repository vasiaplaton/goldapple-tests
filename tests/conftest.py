import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Or use Firefox(), Edge(), etc.
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    yield driver
    # Teardown: Quit browser after test
    driver.quit()
