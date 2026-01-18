"""
Base Page Object class with common WebDriver operations
All page objects inherit from this class
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
import time


class BasePage:
    """Base class for all Page Objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.base_url = Config.BASE_URL
    
    # Navigation methods
    def navigate_to(self, path=""):
        """Navigate to a specific path"""
        url = f"{self.base_url}{path}"
        self.driver.get(url)
    
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    # Element interaction methods
    def find_element(self, locator, timeout=None):
        """
        Find element with explicit wait
        Args:
            locator: Tuple (By.STRATEGY, "value")
            timeout: Optional custom timeout
        """
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout=None):
        """Find multiple elements"""
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    def click(self, locator, timeout=None):
        """Click on element with wait for clickable"""
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type(self, locator, text, timeout=None, clear_first=True):
        """
        Type text into input field
        Args:
            locator: Tuple (By.STRATEGY, "value")
            text: Text to type
            timeout: Optional custom timeout
            clear_first: Clear field before typing
        """
        element = self.find_element(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=None):
        """Get text from element"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def get_attribute(self, locator, attribute, timeout=None):
        """Get attribute value from element"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)
    
    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=5):
        """Check if element is present in DOM"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=None):
        """Wait for element to disappear from DOM"""
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_url_contains(self, url_part, timeout=None):
        """Wait for URL to contain specific string"""
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.url_contains(url_part))
    
    def wait_for_url_to_be(self, url, timeout=None):
        """Wait for URL to be exact match"""
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.url_to_be(url))
    
    # Alert/Modal methods
    def accept_alert(self, timeout=5):
        """Accept JavaScript alert"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            alert.accept()
            return True
        except TimeoutException:
            return False
    
    def dismiss_alert(self, timeout=5):
        """Dismiss JavaScript alert"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            alert.dismiss()
            return True
        except TimeoutException:
            return False
    
    def get_alert_text(self, timeout=5):
        """Get alert text"""
        wait = WebDriverWait(self.driver, timeout)
        alert = wait.until(EC.alert_is_present())
        return alert.text
    
    # Wait helpers
    def wait_for_loading_to_complete(self, timeout=10):
        """Wait for loading spinner to disappear"""
        loading_spinner = (By.CSS_SELECTOR, ".loading-spinner")
        try:
            # Wait for spinner to appear first
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(loading_spinner)
            )
            # Then wait for it to disappear
            self.wait_for_element_to_disappear(loading_spinner, timeout)
        except TimeoutException:
            # Spinner might not appear for fast operations
            pass
    
    def wait(self, seconds):
        """Explicit wait for specified seconds"""
        time.sleep(seconds)
    
    # Screenshot method
    def take_screenshot(self, filename):
        """Take screenshot with custom filename"""
        screenshot_path = Config.get_screenshot_path() / filename
        self.driver.save_screenshot(str(screenshot_path))
        return screenshot_path
    
    # Scroll methods
    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")
