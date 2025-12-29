import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from src.utilities.config import BROWSER, IMPLICIT_WAIT

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@pytest.fixture(scope="function")
def driver():
    """
    PyTest fixture to create and cleanup WebDriver
    Scope: 'function' means new driver for each test
    """
    logging.info("Creating WebDriver")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Explicitly point to your downloaded chromedriver
    service = ChromeService("C:\\Driver\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    # Set implicit wait
    driver.implicitly_wait(IMPLICIT_WAIT)

    logging.info("WebDriver created successfully")

    yield driver  # Provide driver to test

    # Teardown
    logging.info("Closing WebDriver")
    driver.quit()
