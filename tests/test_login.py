import pytest
import logging
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.utilities.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

logger = logging.getLogger(__name__)

@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """Login test cases for ParaBank"""
    
    def test_valid_login(self, driver):
        """
        Test: User should be able to login with valid credentials
        
        Test Steps:
        1. Navigate to ParaBank login page
        2. Enter valid username (john)
        3. Enter valid password (demo1234)
        4. Click Login button
        
        Expected Result: User logged in and sees dashboard
        """
        # Arrange
        login_page = LoginPage(driver)
        driver.get(BASE_URL)
        
        logger.info("TEST START: test_valid_login")
        
        # Act
        login_page.login_with_credentials(VALID_USERNAME, VALID_PASSWORD)
        
        # Assert
        dashboard = DashboardPage(driver)
        assert dashboard.is_logged_in(), "User should be logged in!"
        
        welcome_msg = dashboard.get_welcome_message()
        assert welcome_msg is not None, "Welcome message should be displayed"
        
        logger.info("TEST PASSED: test_valid_login")
    
    def test_invalid_login(self, driver):
        """
        Test: Login should fail with invalid credentials
        
        Expected Result: Error message displayed
        """
        # Arrange
        login_page = LoginPage(driver)
        driver.get(BASE_URL)
        
        logger.info("TEST START: test_invalid_login")
        
        # Act
        login_page.login_with_credentials("invalid", "wrong")
        
        # Assert
        assert login_page.is_error_displayed(), "Error message should be displayed"
        
        error_msg = login_page.get_error_message()
        logger.info(f"Error message: {error_msg}")
        logger.info("TEST PASSED: test_invalid_login")
    
    def test_logout(self, driver):
        """
        Test: User should be able to logout
        
        Test Steps:
        1. Login with valid credentials
        2. Click logout
        3. Verify back on login page
        """
        # Arrange
        login_page = LoginPage(driver)
        driver.get(BASE_URL)
        
        logger.info("TEST START: test_logout")
        
        # Act - Login
        login_page.login_with_credentials(VALID_USERNAME, VALID_PASSWORD)
        dashboard = DashboardPage(driver)
        
        # Assert - Verify logged in
        assert dashboard.is_logged_in(), "User should be logged in"
        
        # Act - Logout
        dashboard.logout()
        login_page.wait(1)
        
        # Assert - Verify back on login page
        assert login_page.is_element_displayed(login_page.USERNAME_INPUT), \
            "Should be back on login page"
        
        logger.info("TEST PASSED: test_logout")
