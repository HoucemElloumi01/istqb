"""
Pytest configuration and fixtures
Provides WebDriver setup, configuration, and test utilities
"""
import pytest
import os
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from config.config import Config


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browser",
        action="store",
        default=Config.DEFAULT_BROWSER,
        help="Browser to use: chrome, firefox, or edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=Config.HEADLESS,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="function")
def browser(request):
    """
    WebDriver fixture - creates and manages browser instance
    Scope: function - new browser for each test
    """
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    
    driver = None
    
    try:
        # Chrome browser
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            # Accept insecure certificates for localhost
            options.add_argument("--ignore-certificate-errors")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            # Selenium 4.6+ automatically manages drivers
            driver = webdriver.Chrome(options=options)
        
        # Firefox browser
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.accept_insecure_certs = True
            
            # Selenium 4.6+ automatically manages drivers
            driver = webdriver.Firefox(options=options)
        
        # Edge browser
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--ignore-certificate-errors")
            
            # Selenium 4.6+ automatically manages drivers
            driver = webdriver.Edge(options=options)
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        # Configure implicit wait
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        
        # Make driver available to test
        yield driver
        
    finally:
        # Teardown: Take screenshot on failure
        if driver and request.node.rep_call.failed and Config.SCREENSHOT_ON_FAILURE:
            take_screenshot(driver, request.node.nodeid)
        
        # Close browser
        if driver:
            driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results for screenshot on failure
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def take_screenshot(driver, test_name):
    """
    Take screenshot and save with test name
    """
    try:
        screenshot_dir = Config.get_screenshot_path()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Clean test name for filename
        clean_name = test_name.replace("::", "_").replace("/", "_").replace("\\", "_")
        screenshot_path = screenshot_dir / f"{clean_name}_{timestamp}.png"
        
        driver.save_screenshot(str(screenshot_path))
        print(f"\n📸 Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"\n❌ Failed to take screenshot: {e}")


@pytest.fixture(scope="session")
def config():
    """
    Configuration fixture - provides access to Config class
    Scope: session - shared across all tests
    """
    return Config


@pytest.fixture
def base_url(config):
    """
    Base URL fixture
    """
    return config.BASE_URL


@pytest.fixture
def test_user_credentials(config):
    """
    Test user credentials fixture
    """
    return {
        "email": config.TEST_USER_EMAIL,
        "password": config.TEST_USER_PASSWORD,
        "username": config.TEST_USER_USERNAME
    }


@pytest.fixture
def admin_user_credentials(config):
    """
    Admin user credentials fixture
    """
    return {
        "email": config.ADMIN_USER_EMAIL,
        "password": config.ADMIN_USER_PASSWORD,
        "username": config.ADMIN_USER_USERNAME
    }
