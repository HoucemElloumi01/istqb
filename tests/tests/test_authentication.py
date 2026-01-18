"""
Authentication Workflow System Tests
Tests: Login, Registration, and Logout workflows

Test Level: System Testing
Test Type: Functional
Techniques Used:
- Equivalence Partitioning (valid/invalid credentials)
- Boundary Value Analysis (password length, email format)
- Decision Table Testing (registration validation)
- Error Guessing (common user mistakes)
"""
import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.menu_page import MenuPage
from data.test_data import TestData, INVALID_EMAILS, INVALID_PASSWORDS, BOUNDARY_VALUES


@pytest.mark.authentication
@pytest.mark.smoke
@pytest.mark.functional
class TestAuthentication:
    """Authentication workflow test cases"""
    
    def test_TC001_valid_login(self, browser, base_url, test_user_credentials):
        """
        TC001: Login with valid credentials
        
        Test Technique: Equivalence Partitioning (Valid class)
        Prerequisites: User account exists in system
        Expected Result: User successfully logs in and redirected to menu page
        """
        # Arrange
        login_page = LoginPage(browser)
        
        # Act
        login_page.navigate()
        login_page.login(
            test_user_credentials['email'],
            test_user_credentials['password']
        )
        
        # Assert
        login_page.wait_for_login_success(timeout=10)
        assert "/menu" in login_page.get_current_url(), "Should redirect to menu page after login"
    
    def test_TC002_invalid_password(self, browser, base_url, test_user_credentials):
        """
        TC002: Login with incorrect password
        
        Test Technique: Equivalence Partitioning (Invalid class)
        Prerequisites: User account exists
        Expected Result: Error message displayed, user remains on login page
        """
        # Arrange
        login_page = LoginPage(browser)
        
        # Act
        login_page.navigate()
        login_page.login(
            test_user_credentials['email'],
            "WrongPassword123!"
        )
        
        # Assert
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_message = login_page.get_error_message()
        assert error_message is not None, "Error message should not be None"
        assert "password" in error_message.lower() or "invalid" in error_message.lower(), \
            "Error message should mention password or invalid credentials"
        assert login_page.is_on_login_page(), "Should remain on login page"
    
    @pytest.mark.parametrize("invalid_email", INVALID_EMAILS[:3])
    def test_TC003_invalid_email_format(self, browser, base_url, invalid_email):
        """
        TC003: Login with invalid email format
        
        Test Technique: Boundary Value Analysis, Error Guessing
        Prerequisites: None
        Expected Result: Validation error or login failure
        """
        # Arrange
        login_page = LoginPage(browser)
        
        # Act
        login_page.navigate()
        login_page.enter_email(invalid_email)
        login_page.enter_password("TestPass123!")
        login_page.click_login_button()
        
        # Assert
        # Either validation prevents submission or login fails
        assert login_page.is_on_login_page() or login_page.is_error_displayed(), \
            "Should either stay on login page or show error"
    
    def test_TC004_empty_credentials(self, browser, base_url):
        """
        TC004: Login with empty email and password
        
        Test Technique: Error Guessing
        Prerequisites: None
        Expected Result: Form validation prevents submission or shows error
        """
        # Arrange
        login_page = LoginPage(browser)
        
        # Act
        login_page.navigate()
        login_page.click_login_button()
        
        # Assert
        assert login_page.is_on_login_page(), "Should remain on login page"
    
    @pytest.mark.regression
    def test_TC005_valid_registration(self, browser, base_url):
        """
        TC005: Register new user with valid data
        
        Test Technique: Decision Table Testing
        Prerequisites: Email not already registered
        Expected Result: Registration successful, redirected to login
        """
        # Arrange
        register_page = RegisterPage(browser)
        test_user = {
            "username": TestData.generate_random_username(),
            "email": TestData.generate_random_email(),
            "phone": "+216 98 " + str(TestData.fake.random_number(digits=6, fix_len=True)),
            "password": "TestPass123!"
        }
        
        # Act
        register_page.navigate()
        register_page.register(
            username=test_user['username'],
            email=test_user['email'],
            phone=test_user['phone'],
            password=test_user['password']
        )
        
        # Assert
        # Either success message or redirect to login
        is_redirected = "/login" in register_page.get_current_url()
        has_success = register_page.is_success_displayed()
        
        assert is_redirected or has_success, \
            "Should show success message or redirect to login page"
    
    def test_TC006_password_mismatch_registration(self, browser, base_url):
        """
        TC006: Register with non-matching passwords
        
        Test Technique: Decision Table Testing (Invalid condition)
        Prerequisites: None
        Expected Result: Validation error for password mismatch
        """
        # Arrange
        register_page = RegisterPage(browser)
        
        # Act
        register_page.navigate()
        register_page.register(
            username=TestData.generate_random_username(),
            email=TestData.generate_random_email(),
            phone="+216 98 123 456",
            password="TestPass123!",
            confirm_password="DifferentPass123!"
        )
        
        # Assert
        # Check for validation error
        validation_errors = register_page.get_validation_errors()
        assert len(validation_errors) > 0 or register_page.is_error_displayed(), \
            "Should show validation error for password mismatch"
    
    def test_TC007_registration_short_password(self, browser, base_url):
        """
        TC007: Register with password below minimum length
        
        Test Technique: Boundary Value Analysis (Below minimum)
        Prerequisites: None
        Expected Result: Validation error for password too short
        """
        # Arrange
        register_page = RegisterPage(browser)
        short_password = BOUNDARY_VALUES['password_below_min']
        
        # Act
        register_page.navigate()
        register_page.register(
            username=TestData.generate_random_username(),
            email=TestData.generate_random_email(),
            phone="+216 98 123 456",
            password=short_password
        )
        
        # Assert
        validation_errors = register_page.get_validation_errors()
        assert len(validation_errors) > 0 or register_page.is_error_displayed(), \
            "Should show validation error for short password"
    
    def test_TC008_navigation_login_to_register(self, browser, base_url):
        """
        TC008: Navigate from login to register page
        
        Test Technique: State Transition Testing
        Prerequisites: None
        Expected Result: Successfully navigate to register page
        """
        # Arrange
        login_page = LoginPage(browser)
        
        # Act
        login_page.navigate()
        login_page.click_register_link()
        
        # Assert
        assert "/register" in browser.current_url, "Should navigate to register page"
    
    def test_TC009_navigation_register_to_login(self, browser, base_url):
        """
        TC009: Navigate from register to login page
        
        Test Technique: State Transition Testing
        Prerequisites: None
        Expected Result: Successfully navigate to login page
        """
        # Arrange
        register_page = RegisterPage(browser)
        
        # Act
        register_page.navigate()
        register_page.click_login_link()
        
        # Assert
        assert "/login" in browser.current_url, "Should navigate to login page"
    
    @pytest.mark.e2e
    def test_TC010_complete_registration_and_login_flow(self, browser, base_url):
        """
        TC010: End-to-end registration and login workflow
        
        Test Technique: Use Case Testing
        Prerequisites: None
        Expected Result: Register new user, then login successfully
        """
        # Arrange
        register_page = RegisterPage(browser)
        login_page = LoginPage(browser)
        test_user = {
            "username": TestData.generate_random_username(),
            "email": TestData.generate_random_email(),
            "phone": "+216 98 " + str(TestData.fake.random_number(digits=6, fix_len=True)),
            "password": "CompleteFlow123!"
        }
        
        # Act - Register
        register_page.navigate()
        register_page.register(
            username=test_user['username'],
            email=test_user['email'],
            phone=test_user['phone'],
            password=test_user['password']
        )
        
        # Wait for redirect or success
        browser.implicitly_wait(3)
        
        # Act - Login with new credentials
        login_page.navigate()
        login_page.login(test_user['email'], test_user['password'])
        
        # Assert
        login_page.wait_for_login_success(timeout=10)
        assert "/menu" in login_page.get_current_url(), \
            "Should successfully login with newly registered credentials"
