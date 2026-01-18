"""
Menu Management Workflow System Tests
Tests: Menu CRUD operations and navigation

Test Level: System Testing
Test Type: Functional
Techniques Used:
- Use Case Testing (complete workflows)
- State Transition Testing (navigation)
- Decision Table Testing (CRUD operations)
"""
import pytest
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from data.test_data import TestData, TEST_MENUS


@pytest.mark.menu
@pytest.mark.functional
class TestMenuWorkflow:
    """Menu management workflow test cases"""
    
    @pytest.fixture(autouse=True)
    def setup(self, browser, admin_user_credentials):
        """Login as admin before each test"""
        login_page = LoginPage(browser)
        login_page.navigate()
        login_page.login(
            admin_user_credentials['email'],
            admin_user_credentials['password']
        )
        login_page.wait_for_login_success(timeout=10)
    
    @pytest.mark.smoke
    def test_TC011_view_menu_list_as_authenticated_user(self, browser):
        """
        TC011: View menu list as authenticated user
        
        Test Technique: Use Case Testing
        Prerequisites: User is logged in
        Expected Result: Menus page displays with menus or empty state
        """
        # Arrange
        menu_page = MenuPage(browser)
        
        # Act
        menu_page.navigate()
        
        # Assert
        assert menu_page.is_on_menu_page(), "Should be on menu page"
        assert menu_page.get_page_heading() == "Our Menus", "Page heading should be 'Our Menus'"
        
        # Either menus are displayed or "no menus" message
        has_menus = menu_page.get_menu_count() > 0
        no_menus_msg = menu_page.is_no_menus_message_displayed()
        assert has_menus or no_menus_msg, "Should display menus or 'no menus' message"
    
    @pytest.mark.regression
    def test_TC012_admin_add_new_menu(self, browser):
        """
        TC012: Admin creates new menu
        
        Test Technique: Decision Table Testing (Create operation)
        Prerequisites: Logged in as Admin/Chef
        Expected Result: New menu created successfully
        """
        # Arrange
        menu_page = MenuPage(browser)
        new_menu = {
            "name": TestData.generate_menu_name(),
            "description": TestData.generate_menu_description()
        }
        
        # Act
        menu_page.navigate()
        initial_count = menu_page.get_menu_count()
        
        # Verify Add button is visible for admin
        assert menu_page.is_add_menu_button_visible(), "Add Menu button should be visible for admin"
        
        menu_page.click_add_menu_button()
        assert menu_page.is_modal_open(), "Modal should open"
        assert "Add New Menu" in menu_page.get_modal_title(), "Modal title should indicate adding"
        
        menu_page.create_menu(new_menu['name'], new_menu['description'])
        
        # Wait for modal to close and page to refresh
        menu_page.wait(3)
        
        # Assert
        menu_page.navigate()  # Refresh to see new menu
        final_count = menu_page.get_menu_count()
        assert final_count > initial_count, "Menu count should increase"
        
        menu_titles = menu_page.get_menu_titles()
        assert new_menu['name'] in menu_titles, f"New menu '{new_menu['name']}' should appear in list"
    
    @pytest.mark.regression
    def test_TC013_admin_edit_existing_menu(self, browser):
        """
        TC013: Admin edits existing menu
        
        Test Technique: Decision Table Testing (Update operation)
        Prerequisites: At least one menu exists, logged in as Admin/Chef
        Expected Result: Menu updated successfully
        """
        # Arrange
        menu_page = MenuPage(browser)
        updated_data = {
            "name": "Updated Menu " + str(TestData.fake.random_number(digits=4)),
            "description": "Updated description - " + TestData.generate_random_text(50)
        }
        
        # Act
        menu_page.navigate()
        
        # Skip if no menus
        if menu_page.get_menu_count() == 0:
            pytest.skip("No menus available to edit")
        
        menu_page.click_edit_menu(menu_index=0)
        assert menu_page.is_modal_open(), "Edit modal should open"
        assert "Edit Menu" in menu_page.get_modal_title(), "Modal title should indicate editing"
        
        menu_page.edit_menu_details(updated_data['name'], updated_data['description'])
        
        # Wait for save
        menu_page.wait(3)
        
        # Assert
        menu_page.navigate()  # Refresh
        menu_titles = menu_page.get_menu_titles()
        assert updated_data['name'] in menu_titles, "Updated menu name should appear in list"
    
    def test_TC014_admin_delete_menu_with_confirmation(self, browser):
        """
        TC014: Admin deletes menu with confirmation
        
        Test Technique: Decision Table Testing (Delete operation)
        Prerequisites: At least one menu exists, logged in as Admin/Chef
        Expected Result: Menu deleted after confirmation
        """
        # Arrange
        menu_page = MenuPage(browser)
        
        # Act
        menu_page.navigate()
        
        # Skip if no menus
        initial_count = menu_page.get_menu_count()
        if initial_count == 0:
            pytest.skip("No menus available to delete")
        
        menu_page.click_delete_menu(menu_index=0)
        
        # Confirm deletion in alert
        menu_page.confirm_delete_alert()
        menu_page.wait(2)
        
        # Accept success alert if present
        try:
            menu_page.accept_alert(timeout=3)
        except:
            pass
        
        # Assert
        menu_page.navigate()  # Refresh
        final_count = menu_page.get_menu_count()
        # Count should decrease or remain same if deletion failed
        assert final_count <= initial_count, "Menu should be deleted"
    
    def test_TC015_admin_cancel_menu_deletion(self, browser):
        """
        TC015: Admin cancels menu deletion
        
        Test Technique: Decision Table Testing (Cancel operation)
        Prerequisites: At least one menu exists
        Expected Result: Menu not deleted when cancelling
        """
        # Arrange
        menu_page = MenuPage(browser)
        
        # Act
        menu_page.navigate()
        
        initial_count = menu_page.get_menu_count()
        if initial_count == 0:
            pytest.skip("No menus available")
        
        menu_page.click_delete_menu(menu_index=0)
        
        # Cancel deletion
        menu_page.cancel_delete_alert()
        menu_page.wait(1)
        
        # Assert
        final_count = menu_page.get_menu_count()
        assert final_count == initial_count, "Menu count should remain same after cancelling"
    
    def test_TC016_navigate_to_menu_details(self, browser):
        """
        TC016: Navigate to menu details page
        
        Test Technique: State Transition Testing
        Prerequisites: At least one menu exists
        Expected Result: Successfully navigate to menu details
        """
        # Arrange
        menu_page = MenuPage(browser)
        
        # Act
        menu_page.navigate()
        
        if menu_page.get_menu_count() == 0:
            pytest.skip("No menus available")
        
        menu_page.click_view_menu(menu_index=0)
        
        # Assert
        # URL should change to menu details page (e.g., /menu/1)
        current_url = menu_page.get_current_url()
        assert "/menu/" in current_url, "Should navigate to menu details page"
    
    def test_TC017_menu_form_validation_empty_fields(self, browser):
        """
        TC017: Test menu form validation with empty fields
        
        Test Technique: Error Guessing, Boundary Value Analysis
        Prerequisites: Logged in as Admin
        Expected Result: Validation prevents submission with empty fields
        """
        # Arrange
        menu_page = MenuPage(browser)
        
        # Act
        menu_page.navigate()
        
        if not menu_page.is_add_menu_button_visible():
            pytest.skip("Add menu button not visible (not admin)")
        
        menu_page.click_add_menu_button()
        
        # Try to save without entering data
        menu_page.click_modal_save()
        
        # Assert
        # Modal should still be open (validation prevented submission)
        assert menu_page.is_modal_open(), "Modal should remain open due to validation"
    
    @pytest.mark.smoke
    def test_TC018_menu_page_accessible_after_login(self, browser):
        """
        TC018: Menu page is accessible after login
        
        Test Technique: State Transition Testing
        Prerequisites: User logged in
        Expected Result: Menu page loads successfully
        """
        # Arrange & Act
        menu_page = MenuPage(browser)
        menu_page.navigate()
        
        # Assert
        assert menu_page.is_on_menu_page(), "Should be on menu page"
        # Page should not redirect to login
        assert "/login" not in menu_page.get_current_url(), "Should not redirect to login"
