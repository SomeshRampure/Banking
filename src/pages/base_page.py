from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logger = logging.getLogger(__name__)

class BasePage:
    """
    Base class for all page objects.
    Contains common methods needed by all pages.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_driver = WebDriverWait(driver, 10)
    
    # ============ WAIT METHODS ============
    
    def wait_for_element_clickable(self, locator, timeout=10):
        """Wait for element to be clickable"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            logger.info(f"Element clickable: {locator}")
            return element
        except:
            logger.error(f"Element not clickable: {locator}")
            raise
    
    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element visible: {locator}")
            return element
        except:
            logger.error(f"Element not visible: {locator}")
            raise
    
    # ============ CLICK & TYPE METHODS ============
    
    def click_element(self, locator):
        """Click on element"""
        try:
            element = self.wait_driver.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Clicked: {locator}")
        except Exception as e:
            logger.error(f"Failed to click: {locator}")
            raise
    
    def send_keys(self, locator, text):
        """Enter text into element"""
        try:
            element = self.wait_driver.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"Entered text: {text}")
        except Exception as e:
            logger.error(f"Failed to enter text: {locator}")
            raise
    
    # ============ GET TEXT & ATTRIBUTE METHODS ============
    
    def get_text(self, locator):
        """Get text from element"""
        try:
            element = self.wait_driver.until(EC.element_to_be_clickable(locator))
            text = element.text
            logger.info(f"Got text: {text}")
            return text
        except:
            logger.error(f"Failed to get text: {locator}")
            raise
    
    def get_attribute(self, locator, attribute_name):
        """Get attribute value from element"""
        try:
            element = self.wait_driver.until(EC.element_to_be_clickable(locator))
            value = element.get_attribute(attribute_name)
            logger.info(f"Got attribute {attribute_name}: {value}")
            return value
        except:
            logger.error(f"Failed to get attribute: {locator}")
            raise
    
    # ============ CHECK ELEMENT STATE METHODS ============
    
    def is_element_displayed(self, locator):
        """Check if element is visible"""
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False
    
    def is_element_enabled(self, locator):
        """Check if element is enabled"""
        try:
            element = self.driver.find_element(*locator)
            return element.is_enabled()
        except:
            return False
    
    # ============ NAVIGATION METHODS ============
    
    def go_to_url(self, url):
        """Navigate to URL"""
        try:
            self.driver.get(url)
            logger.info(f"Navigated to: {url}")
        except:
            logger.error(f"Failed to navigate to: {url}")
            raise
    
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
    
    def refresh_page(self):
        """Refresh current page"""
        self.driver.refresh()
        logger.info("Page refreshed")
    
    # ============ WAIT TIME ============
    
    def wait(self, seconds):
        """Explicit wait (use sparingly)"""
        time.sleep(seconds)
        logger.info(f"Waited {seconds} seconds")