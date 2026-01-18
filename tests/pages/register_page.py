"""
Register Page Object
Represents the registration page and its interactions
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Register page object model"""
    
    # Locators
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='johndoe']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder*='example.com']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='216'], input[placeholder*='phone' i]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][placeholder*='••••••••']:first-of-type")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][placeholder*='••••••••']:last-of-type")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-error")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    VALIDATION_ERROR = (By.CSS_SELECTOR, ".text-red-500")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_path = "/register"
    
    def navigate(self):
        """Navigate to register page"""
        self.navigate_to(self.page_path)
        return self
    
    def enter_username(self, username):
        """Enter username"""
        self.type(self.USERNAME_INPUT, username)
        return self
    
    def enter_email(self, email):
        """Enter email"""
        self.type(self.EMAIL_INPUT, email)
        return self
    
    def enter_phone(self, phone):
        """Enter phone number"""
        self.type(self.PHONE_INPUT, phone)
        return self
    
    def enter_password(self, password):
        """Enter password"""
        self.type(self.PASSWORD_INPUT, password)
        return self
    
    def enter_confirm_password(self, password):
        """Enter confirmation password"""
        self.type(self.CONFIRM_PASSWORD_INPUT, password)
        return self
    
    def click_register_button(self):
        """Click register button"""
        self.click(self.REGISTER_BUTTON)
        return self
    
    def register(self, username, email, phone, password, confirm_password=None):
        """
        Complete registration flow
        Args:
            username: Username
            email: Email address
            phone: Phone number
            password: Password
            confirm_password: Confirmation password (defaults to password if not provided)
        """
        if confirm_password is None:
            confirm_password = password
        
        self.enter_username(username)
        self.enter_email(email)
        self.enter_phone(phone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_register_button()
        # Wait for processing
        self.wait(2)
        return self
    
    def click_login_link(self):
        """Click on login link"""
        self.click(self.LOGIN_LINK)
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
    
    def get_validation_errors(self):
        """Get all validation error messages"""
        if self.is_element_present(self.VALIDATION_ERROR, timeout=2):
            errors = self.find_elements(self.VALIDATION_ERROR, timeout=2)
            return [error.text for error in errors if error.text]
        return []
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=3)
    
    def is_success_displayed(self):
        """Check if success message is displayed"""
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=3)
    
    def wait_for_registration_success(self, timeout=10):
        """Wait for successful registration redirect"""
        self.wait_for_url_contains("/login", timeout=timeout)
        return self
    
    def is_on_register_page(self):
        """Verify current page is register page"""
        return "/register" in self.get_current_url()
    
    def get_page_heading(self):
        """Get page heading text"""
        return self.get_text(self.PAGE_TITLE)
