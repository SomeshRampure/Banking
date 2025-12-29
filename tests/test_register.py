import pytest
import logging
from src.pages.register_page import RegisterPage
from src.utilities.config import BASE_URL

logger = logging.getLogger(__name__)

@pytest.mark.register
@pytest.mark.smoke
class TestRegister:
    """Register test cases for ParaBank"""
    
    def test_register_link(self, driver):
        """
        Test: Register link should navigate to registration page
        
        Test Steps:
        1. Navigate to ParaBank home page
        2. Click on Register link
        
        Expected Result: Registration page is displayed
        """
        # Arrange
        register_page = RegisterPage(driver)
        driver.get(BASE_URL)

        logger.info("TEST START: test_register_link")

        # Act
        register_page.click_register()

        # Assert
        assert "Register" in driver.title, "Registration page should be displayed"

        logger.info("TEST PASSED: test_register_link")