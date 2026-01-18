"""
End-to-End System Tests
Tests: Complete user journeys and workflows

Test Level: System Testing
Test Type: Functional (E2E scenarios)
Techniques Used:
- Use Case Testing (complete user stories)
- Exploratory Testing approach
"""
import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.menu_page import MenuPage
from data.test_data import TestData


@pytest.mark.e2e
@pytest.mark.functional
class TestEndToEnd:
    """End-to-end scenario test cases"""
    
    @pytest.mark.slow
    def test_TC019_complete_customer_registration_and_menu_browsing(self, browser, base_url):
        """
        TC019: Complete customer journey - Register, Login, Browse Menus
        
        Test Technique: Use Case Testing (User Story)
        Prerequisites: None
        Expected Result: User can complete entire workflow from registration to browsing
        
        User Story:
        As a new customer, I want to register an account, login,
        and browse available menus
        """
        # Arrange
        register_page = RegisterPage(browser)
        login_page = LoginPage(browser)
        menu_page = MenuPage(browser)
        
        test_user = {
            "username": TestData.generate_random_username(),
            "email": TestData.generate_random_email(),
            "phone": "+216 98 " + str(TestData.fake.random_number(digits=6, fix_len=True)),
            "password": "E2ETest123!"
        }
        
        # Step 1: Register new account
        register_page.navigate()
        assert register_page.is_on_register_page(), "Should be on register page"
        
        register_page.register(
            username=test_user['username'],
            email=test_user['email'],
            phone=test_user['phone'],
            password=test_user['password']
        )
        
        # Wait for registration to complete
        browser.implicitly_wait(3)
        
        # Step 2: Login with new credentials
        login_page.navigate()
        assert login_page.is_on_login_page(), "Should be on login page"
        
        login_page.login(test_user['email'], test_user['password'])
        login_page.wait_for_login_success(timeout=10)
        
        # Step 3: Browse menus
        assert menu_page.is_on_menu_page(), "Should be redirected to menu page after login"
        
        page_heading = menu_page.get_page_heading()
        assert "Menu" in page_heading, "Menu page should display proper heading"
        
        # Check menus are displayed or no menus message
        has_menus = menu_page.get_menu_count() > 0
        no_menus = menu_page.is_no_menus_message_displayed()
        assert has_menus or no_menus, "Should display menus or 'no menus' message"
        
        print(f"✓ E2E Flow Complete: Registered user '{test_user['username']}', logged in, and browsed menus")
    
    @pytest.mark.slow
    def test_TC020_admin_complete_menu_management_workflow(self, browser, admin_user_credentials):
        """
        TC020: Complete admin workflow - Login, Create Menu, Edit Menu
        
        Test Technique: Use Case Testing (Admin Story)
        Prerequisites: Admin account exists
        Expected Result: Admin can perform complete menu management workflow
        
        User Story:
        As an admin, I want to login, create a new menu,
        and edit it to update information
        """
        # Arrange
        login_page = LoginPage(browser)
        menu_page = MenuPage(browser)
        
        new_menu = {
            "name": "E2E Test Menu " + str(TestData.fake.random_number(digits=4)),
            "description": "Created during E2E testing"
        }
        
        updated_menu = {
            "name": new_menu['name'] + " (Updated)",
            "description": "Updated during E2E testing"
        }
        
        # Step 1: Login as admin
        login_page.navigate()
        login_page.login(
            admin_user_credentials['email'],
            admin_user_credentials['password']
        )
        login_page.wait_for_login_success()
        
        # Step 2: Navigate to menus
        menu_page.navigate()
        assert menu_page.is_on_menu_page(), "Should be on menu page"
        assert menu_page.is_add_menu_button_visible(), "Admin should see Add Menu button"
        
        initial_count = menu_page.get_menu_count()
        
        # Step 3: Create new menu
        menu_page.click_add_menu_button()
        assert menu_page.is_modal_open(), "Create menu modal should open"
        
        menu_page.create_menu(new_menu['name'], new_menu['description'])
        menu_page.wait(3)
        
        # Verify creation
        menu_page.navigate()
        assert menu_page.get_menu_count() > initial_count, "New menu should be created"
        assert new_menu['name'] in menu_page.get_menu_titles(), "New menu should appear in list"
        
        # Step 4: Edit the created menu
        # Find the index of our newly created menu
        menu_titles = menu_page.get_menu_titles()
        menu_index = menu_titles.index(new_menu['name']) if new_menu['name'] in menu_titles else 0
        
        menu_page.click_edit_menu(menu_index)
        assert menu_page.is_modal_open(), "Edit menu modal should open"
        
        menu_page.edit_menu_details(updated_menu['name'], updated_menu['description'])
        menu_page.wait(3)
        
        # Verify update
        menu_page.navigate()
        assert updated_menu['name'] in menu_page.get_menu_titles(), "Menu should be updated"
        
        print(f"✓ E2E Admin Flow Complete: Created and updated menu '{updated_menu['name']}'")
    
    def test_TC021_login_to_menu_navigation_workflow(self, browser, test_user_credentials):
        """
        TC021: Login and navigate through menu structure
        
        Test Technique: State Transition Testing
        Prerequisites: Test user exists
        Expected Result: User can login and navigate menu hierarchy
        """
        # Arrange
        login_page = LoginPage(browser)
        menu_page = MenuPage(browser)
        
        # Step 1: Login
        login_page.navigate()
        login_page.login(
            test_user_credentials['email'],
            test_user_credentials['password']
        )
        login_page.wait_for_login_success()
        
        # Step 2: Verify on menu page
        assert menu_page.is_on_menu_page(), "Should be on menu page after login"
        
        # Step 3: If menus exist, navigate to one
        if menu_page.get_menu_count() > 0:
            menu_page.click_view_menu(0)
            menu_page.wait(2)
            
            # Verify navigation
            current_url = menu_page.get_current_url()
            assert "/menu/" in current_url, "Should navigate to menu details"
        
        print("✓ Navigation workflow complete")
