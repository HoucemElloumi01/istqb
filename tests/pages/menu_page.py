"""
Menu Page Object
Represents the menu listing page and its interactions
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):
    """Menu page object model"""
    
    # Locators
    PAGE_HEADING = (By.CSS_SELECTOR, "h1")
    ADD_MENU_BUTTON = (By.XPATH, "//button[contains(., 'Add New Menu')]")
    MENU_CARDS = (By.CSS_SELECTOR, ".card")
    LOADING_SPINNER = (By.CSS_SELECTOR, ".loading-spinner")
    NO_MENUS_MESSAGE = (By.XPATH, "//*[contains(text(), 'No menus available')]")
    
    # Modal locators
    MODAL = (By.CSS_SELECTOR, ".modal-open")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-box h3")
    MODAL_NAME_INPUT = (By.CSS_SELECTOR, ".modal-box input[type='text']")
    MODAL_DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, ".modal-box textarea")
    MODAL_SAVE_BUTTON = (By.XPATH, "//div[@class='modal-box']//button[contains(text(), 'Save')]")
    MODAL_CANCEL_BUTTON = (By.XPATH, "//div[@class='modal-box']//button[contains(text(), 'Cancel')]")
    MODAL_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".modal-box .alert-success")
    MODAL_ERROR_MESSAGE = (By.CSS_SELECTOR, ".modal-box .alert-error")
    
    # Menu card elements
    MENU_TITLE = (By.CSS_SELECTOR, ".card-title")
    MENU_DESCRIPTION = (By.CSS_SELECTOR, ".card-body p")
    VIEW_MENU_BUTTON = (By.XPATH, "//a[contains(., 'View Menu')]")
    MENU_OPTIONS_DROPDOWN = (By.CSS_SELECTOR, ".dropdown-end label")
    EDIT_OPTION = (By.XPATH, "//a[contains(text(), 'Edit')]")
    DELETE_OPTION = (By.XPATH, "//a[contains(text(), 'Delete')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_path = "/menu"
    
    def navigate(self):
        """Navigate to menu page"""
        self.navigate_to(self.page_path)
        # Wait for page to load
        self.wait(2)
        return self
    
    def is_on_menu_page(self):
        """Verify current page is menu page"""
        return "/menu" in self.get_current_url()
    
    def get_page_heading(self):
        """Get page heading text"""
        return self.get_text(self.PAGE_HEADING)
    
    def is_add_menu_button_visible(self):
        """Check if Add Menu button is visible (admin/chef only)"""
        return self.is_element_visible(self.ADD_MENU_BUTTON, timeout=3)
    
    def click_add_menu_button(self):
        """Click Add New Menu button"""
        self.click(self.ADD_MENU_BUTTON)
        self.wait_for_modal_to_open()
        return self
    
    def get_menu_count(self):
        """Get number of menus displayed"""
        if self.is_no_menus_message_displayed():
            return 0
        if self.is_element_present(self.MENU_CARDS, timeout=3):
            return len(self.find_elements(self.MENU_CARDS))
        return 0
    
    def is_no_menus_message_displayed(self):
        """Check if 'no menus' message is displayed"""
        return self.is_element_visible(self.NO_MENUS_MESSAGE, timeout=3)
    
    def get_menu_titles(self):
        """Get list of all menu titles"""
        if self.get_menu_count() == 0:
            return []
        titles = self.find_elements(self.MENU_TITLE)
        return [title.text for title in titles]
    
    def click_view_menu(self, menu_index=0):
        """Click View Menu button for specific menu"""
        view_buttons = self.find_elements(self.VIEW_MENU_BUTTON)
        if menu_index < len(view_buttons):
            view_buttons[menu_index].click()
            self.wait(2)
        return self
    
    def click_menu_options_dropdown(self, menu_index=0):
        """Click options dropdown for specific menu"""
        dropdowns = self.find_elements(self.MENU_OPTIONS_DROPDOWN)
        if menu_index < len(dropdowns):
            dropdowns[menu_index].click()
            self.wait(0.5)
        return self
    
    def click_edit_menu(self, menu_index=0):
        """Edit specific menu"""
        self.click_menu_options_dropdown(menu_index)
        self.click(self.EDIT_OPTION)
        self.wait_for_modal_to_open()
        return self
    
    def click_delete_menu(self, menu_index=0):
        """Delete specific menu"""
        self.click_menu_options_dropdown(menu_index)
        self.click(self.DELETE_OPTION)
        return self
    
    # Modal methods
    def is_modal_open(self):
        """Check if modal is open"""
        return self.is_element_visible(self.MODAL, timeout=3)
    
    def wait_for_modal_to_open(self, timeout=5):
        """Wait for modal to open"""
        self.find_element(self.MODAL, timeout=timeout)
        return self
    
    def get_modal_title(self):
        """Get modal title"""
        return self.get_text(self.MODAL_TITLE)
    
    def enter_menu_name(self, name):
        """Enter menu name in modal"""
        self.type(self.MODAL_NAME_INPUT, name)
        return self
    
    def enter_menu_description(self, description):
        """Enter menu description in modal"""
        self.type(self.MODAL_DESCRIPTION_TEXTAREA, description)
        return self
    
    def click_modal_save(self):
        """Click Save button in modal"""
        self.click(self.MODAL_SAVE_BUTTON)
        self.wait(2)  # Wait for save operation
        return self
    
    def click_modal_cancel(self):
        """Click Cancel button in modal"""
        self.click(self.MODAL_CANCEL_BUTTON)
        return self
    
    def create_menu(self, name, description):
        """
        Complete flow to create a new menu
        Assumes modal is already open
        """
        self.enter_menu_name(name)
        self.enter_menu_description(description)
        self.click_modal_save()
        return self
    
    def edit_menu_details(self, name, description):
        """
        Edit menu details
        Assumes modal is already open
        """
        self.enter_menu_name(name)
        self.enter_menu_description(description)
        self.click_modal_save()
        return self
    
    def get_modal_success_message(self):
        """Get success message from modal"""
        if self.is_element_visible(self.MODAL_SUCCESS_MESSAGE, timeout=3):
            return self.get_text(self.MODAL_SUCCESS_MESSAGE)
        return None
    
    def get_modal_error_message(self):
        """Get error message from modal"""
        if self.is_element_visible(self.MODAL_ERROR_MESSAGE, timeout=3):
            return self.get_text(self.MODAL_ERROR_MESSAGE)
        return None
    
    def confirm_delete_alert(self):
        """Confirm deletion in JavaScript alert"""
        return self.accept_alert()
    
    def cancel_delete_alert(self):
        """Cancel deletion in JavaScript alert"""
        return self.dismiss_alert()
