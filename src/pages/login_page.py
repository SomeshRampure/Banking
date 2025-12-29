from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    """Login page object for ParaBank"""
    
    # ============ LOCATORS (Element selectors for ParaBank) ============
    
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//input[@value='Log In']")
    ERROR_MSG = (By.CSS_SELECTOR, ".error")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    
    # ============ METHODS ============
    
    def enter_username(self, username):
        """Enter username"""
        self.send_keys(self.USERNAME_INPUT, username)
        logger.info(f"Entered username: {username}")
    
    def enter_password(self, password):
        """Enter password"""
        self.send_keys(self.PASSWORD_INPUT, password)
        logger.info("Entered password")
    
    def click_login(self):
        """Click Login button"""
        self.click_element(self.LOGIN_BTN)
        logger.info("Clicked Login button")
        self.wait(2)  # Wait for page to load
    
    def login_with_credentials(self, username, password):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        logger.info("Login completed")

    def click_register(self):
        """Click Register Link"""
        self.click_element(self.REGISTER_LINK)
        logger.info ("Clicked Register link")
        self.wait(2)
    
    def is_error_displayed(self):
        """Check if error message is shown"""
        return self.is_element_displayed(self.ERROR_MSG)
    
    def get_error_message(self):
        """Get error message text"""
        try:
            return self.get_text(self.ERROR_MSG)
        except:
            return None
