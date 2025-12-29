import pytest
import os
import subprocess
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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
    
    # Setup: Create Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    # Set implicit wait
    driver.implicitly_wait(IMPLICIT_WAIT)
    
    logging.info("WebDriver created successfully")
    
    yield driver  # Return driver to test
    
    # Teardown: Close driver after test
    logging.info("Closing WebDriver")
    driver.quit()
