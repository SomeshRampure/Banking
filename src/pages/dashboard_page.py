from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class DashboardPage(BasePage):
    """Dashboard page after successful login"""
    
    # ============ LOCATORS ============
    
    WELCOME_MSG = (By.XPATH, "//h1[contains(text(), 'Accounts Overview')]")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")
    
    # ============ METHODS ============
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return self.is_element_displayed(self.WELCOME_MSG)
    
    def get_welcome_message(self):
        """Get welcome message"""
        try:
            return self.get_text(self.WELCOME_MSG)
        except:
            return None
    
    def logout(self):
        """Click logout link"""
        self.click_element(self.LOGOUT_LINK)
        logger.info("Clicked logout")
        self.wait(1)
