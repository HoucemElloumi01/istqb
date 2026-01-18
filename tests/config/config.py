"""
Configuration management for test suite
Loads settings from environment variables with defaults
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)


class Config:
    """Test configuration settings"""
    
    # Application URLs
    BASE_URL = os.getenv('BASE_URL', 'https://localhost:7000')
    
    # Test User Credentials
    TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL', 'testuser@goldenfork.com')
    TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'TestPass123!')
    TEST_USER_USERNAME = os.getenv('TEST_USER_USERNAME', 'testuser')
    
    # Admin Credentials
    ADMIN_USER_EMAIL = os.getenv('ADMIN_USER_EMAIL', 'admin@goldenfork.com')
    ADMIN_USER_PASSWORD = os.getenv('ADMIN_USER_PASSWORD', 'AdminPass123!')
    ADMIN_USER_USERNAME = os.getenv('ADMIN_USER_USERNAME', 'adminuser')
    
    # Browser Configuration
    DEFAULT_BROWSER = os.getenv('DEFAULT_BROWSER', 'chrome').lower()
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '20'))
    
    # Screenshot Configuration
    SCREENSHOT_ON_FAILURE = os.getenv('SCREENSHOT_ON_FAILURE', 'true').lower() == 'true'
    SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR', 'screenshots')
    
    # Test Configuration
    CREATE_TEST_USERS = os.getenv('CREATE_TEST_USERS', 'true').lower() == 'true'
    CLEANUP_TEST_DATA = os.getenv('CLEANUP_TEST_DATA', 'false').lower() == 'true'
    
    @classmethod
    def get_screenshot_path(cls):
        """Get absolute path for screenshots directory"""
        screenshot_dir = Path(__file__).parent.parent / cls.SCREENSHOT_DIR
        screenshot_dir.mkdir(exist_ok=True)
        return screenshot_dir
    
    @classmethod
    def get_reports_path(cls):
        """Get absolute path for reports directory"""
        reports_dir = Path(__file__).parent.parent / 'reports'
        reports_dir.mkdir(exist_ok=True)
        return reports_dir
