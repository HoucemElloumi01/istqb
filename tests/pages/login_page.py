"""
Login Page Object
Represents the login page and its interactions
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object model"""
    
    # Locators
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='text'][placeholder*='example.com'], input[placeholder*='example.com']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-error")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    LOADING_SPINNER = (By.CSS_SELECTOR, ".loading-spinner")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_path = "/login"
    
    def navigate(self):
        """Navigate to login page"""
        self.navigate_to(self.page_path)
        return self
    
    def enter_email(self, email):
        """Enter email in email field"""
        self.type(self.EMAIL_INPUT, email)
        return self
    
    def enter_password(self, password):
        """Enter password in password field"""
        self.type(self.PASSWORD_INPUT, password)
        return self
    
    def click_login_button(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
        return self
    
    def login(self, email, password):
        """
        Complete login flow
        Args:
            email: User email
            password: User password
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        # Wait for either success (redirect) or error message
        self.wait(2)  # Small wait for Blazor to process
        return self
    
    def click_register_link(self):
        """Click on register link"""
        self.click(self.REGISTER_LINK)
        return self
    
    def get_error_message(self):
        """Get error message text"""
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def get_success_message(self):
        """Get success message text"""
        if self.is_element_visible(self.SUCCESS_MESSAGE, timeout=3):
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=3)
    
    def is_success_displayed(self):
        """Check if success message is displayed"""
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=3)
    
    def wait_for_login_success(self, timeout=10):
        """Wait for successful login redirect to menu page"""
        self.wait_for_url_contains("/menu", timeout=timeout)
        return self
    
    def is_on_login_page(self):
        """Verify current page is login page"""
        return "/login" in self.get_current_url()
    
    def get_page_heading(self):
        """Get page heading text"""
        return self.get_text(self.PAGE_TITLE)
