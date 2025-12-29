import logging
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class RegisterPage(BasePage):    
    """Register page object for ParaBank"""

 # ============ LOCATORS (Element selectors for ParaBank) =1===========
    
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "(.//input[@class='button'])[2]")
    ERROR_MSG = (By.CSS_SELECTOR, ".error")

    # ============ METHODS ============
    def click_register(self):
        """Click Register Link"""
        self.click_element(self.REGISTER_LINK)
        logger.info ("Clicked Register link")
        self.wait(2)

    def first_name(self, first_name):
        """Enter First Name"""
        self.send_keys(self.FIRST_NAME, first_name)
        logger.info(f"Entered First Name: {first_name}")

    def last_name(self, last_name):
        """Enter Last Name"""
        self.send_keys(self.LAST_NAME, last_name)
        logger.info(f"Entered Last Name: {last_name}")
    
    def address(self, address):
        """Enter Address"""
        self.send_keys(self.ADDRESS, address)
        logger.info(f"Entered Address: {address}")

    def city(self, city):
        """Enter City"""
        self.send_keys(self.CITY, city)
        logger.info(f"Entered City: {city}")

    def state(self, state):
        """Enter State"""
        self.send_keys(self.STATE, state)
        logger.info(f"Entered State: {state}")

    def is_error_displayed(self):
        """Check if error message is shown"""
        return self.is_element_displayed(self.ERROR_MSG)
    
    def get_error_message(self):
        """Get error message text"""
        try:
            return self.get_text(self.ERROR_MSG)
        except:
            return None