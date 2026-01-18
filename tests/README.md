# Golden Fork - Automated System Tests

![Tests](https://img.shields.io/badge/tests-automated-brightgreen)
![Framework](https://img.shields.io/badge/framework-pytest-blue)
![Selenium](https://img.shields.io/badge/selenium-4.16.0-green)

## 📋 Overview

This is a comprehensive automated test suite for **The Golden Fork** restaurant management application, developed following **ISTQB** guidelines for the Test et Qualité Logiciel module.

### Test Characteristics
- **Test Level**: System Testing
- **Test Type**: Functional (Frontend)
- **Automation Framework**: Selenium WebDriver + pytest
- **Design Pattern**: Page Object Model (POM)
- **Test Techniques**: Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, State Transition Testing

## 🎯 Test Coverage

### Workflows Tested
✅ **Authentication** (10 test cases)
- Login with valid/invalid credentials
- Registration with validation
- Password strength testing
- Navigation between login/register

✅ **Menu Management** (8 test cases)
- View menu list
- Create new menus (Admin/Chef)
- Edit existing menus
- Delete menus with confirmation
- Form validation

✅ **End-to-End Scenarios** (3 test cases)
- Complete customer journey (Register → Login → Browse)
- Admin workflow (Create → Edit menus)
- Navigation workflows

**Total: 21+ Automated Test Cases**

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- The Golden Fork application running locally

### Installation

1. **Navigate to tests directory**
```powershell
cd "c:\Users\houce\OneDrive\Bureau\projet istqb\The-Golden-Fork\tests"
```

2. **Create virtual environment** (recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```powershell
pip install -r requirements.txt
```

4. **Configure environment**
```powershell
# Copy the example environment file
copy .env.example .env

# Edit .env file with your application URL and credentials
notepad .env
```

### Configuration

Edit the `.env` file with your application settings:

```env
# Application URL
BASE_URL=https://localhost:7000

# Test credentials
TEST_USER_EMAIL=testuser@goldenfork.com
TEST_USER_PASSWORD=TestPass123!

ADMIN_USER_EMAIL=admin@goldenfork.com
ADMIN_USER_PASSWORD=AdminPass123!
```

## 🧪 Running Tests

### Run All Tests
```powershell
pytest
```

### Run with HTML Report
```powershell
pytest --html=reports/test_report.html --self-contained-html
```

### Run Specific Test Suite
```powershell
# Authentication tests only
pytest tests/test_authentication.py -v

# Menu workflow tests only
pytest tests/test_menu_workflow.py -v

# End-to-end tests only
pytest tests/test_end_to_end.py -v
```

### Run by Test Markers
```powershell
# Smoke tests only
pytest -m smoke

# Regression suite
pytest -m regression

# End-to-end scenarios
pytest -m e2e

# Authentication tests
pytest -m authentication
```

### Run with Different Browsers
```powershell
# Chrome (default)
pytest --browser=chrome

# Firefox
pytest --browser=firefox

# Edge
pytest --browser=edge

# Headless mode
pytest --headless
```

### Run Specific Test
```powershell
pytest tests/test_authentication.py::TestAuthentication::test_TC001_valid_login -v
```

### Parallel Execution
```powershell
pytest -n 4  # Run with 4 parallel workers
```

## 📁 Project Structure

```
tests/
│
├── config/                     # Configuration management
│   ├── __init__.py
│   └── config.py              # Config class for environment variables
│
├── data/                       # Test data
│   ├── __init__.py
│   └── test_data.py           # Test data generators and constants
│
├── pages/                      # Page Object Model
│   ├── __init__.py
│   ├── base_page.py           # Base page with common methods
│   ├── login_page.py          # Login page object
│   ├── register_page.py       # Register page object
│   └── menu_page.py           # Menu page object
│
├── tests/                      # Test cases
│   ├── __init__.py
│   ├── test_authentication.py # Authentication workflow tests
│   ├── test_menu_workflow.py  # Menu management tests
│   └── test_end_to_end.py     # End-to-end scenarios
│
├── documentation/              # Test documentation
│   ├── test_cases.md          # Documented test cases
│   └── traceability_matrix.md # Requirements traceability
│
├── reports/                    # Test execution reports (generated)
├── screenshots/                # Failure screenshots (generated)
│
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── conftest.py                # Pytest fixtures and configuration
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 📊 Test Techniques Used

### Black-Box Techniques
- **Equivalence Partitioning**: Valid/invalid input classes (login credentials, form data)
- **Boundary Value Analysis**: Min/max lengths for passwords, usernames
- **Decision Table Testing**: Registration validation, CRUD operations
- **State Transition Testing**: Navigation between pages, workflow states
- **Use Case Testing**: End-to-end user journeys

### Test Design
Each test case documents:
- Test ID and title
- Test technique used
- Prerequisites
- Test data
- Expected results
- Actual results (after execution)

## 📝 Test Case Documentation

### Example Test Case Format

```
ID: TC001
Title: Login with valid credentials
Technique: Equivalence Partitioning (Valid class)
Priority: High
Prerequisites: User account exists

Test Data:
- Email: testuser@goldenfork.com
- Password: TestPass123!

Steps:
1. Navigate to login page
2. Enter valid email
3. Enter valid password
4. Click login button

Expected Result:
- User redirected to /menu page
- No error messages displayed

Actual Result: Pass ✓
```

Full documentation available in `documentation/test_cases.md`

## 🔧 Troubleshooting

### Common Issues

**"WebDriver not found"**
- The webdriver-manager should auto-download drivers
- Ensure internet connection for first run

**"Connection refused"**
- Ensure The Golden Fork application is running
- Check BASE_URL in .env matches your app URL

**"Element not found"**
- Application might be loading slowly
- Increase timeout in config.py
- Check if UI elements have changed

**"SSL Certificate Error"**
- For localhost HTTPS, browsers accept insecure certificates
- Configuration already includes --ignore-certificate-errors

### Debug Mode
```powershell
# Run with verbose output and no capture
pytest -v -s

# Run single test with detailed output
pytest tests/test_authentication.py::TestAuthentication::test_TC001_valid_login -v -s
```

## 📈 Continuous Integration

### GitHub Actions Example
```yaml
name: Automated Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          cd tests
          pip install -r requirements.txt
      - name: Run tests
        run: |
          cd tests
          pytest --html=reports/test_report.html
      - name: Upload test report
        uses: actions/upload-artifact@v2
        with:
          name: test-report
          path: tests/reports/
```

## 🎓 ISTQB Compliance

This test suite follows ISTQB guidelines:

✅ **Test Levels**: System testing  
✅ **Test Types**: Functional testing  
✅ **Test Techniques**: Black-box (EP, BVA, Decision Tables, State Transitions)  
✅ **Test Design**: Structured test cases with clear documentation  
✅ **Test Automation**: Selenium + pytest with POM pattern  
✅ **Traceability**: Requirements → Test Cases → Results  
✅ **Reporting**: HTML reports with screenshots on failure  

## 📚 Additional Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://selenium-python.readthedocs.io/page-objects.html)
- [ISTQB Glossary](https://glossary.istqb.org/)

## 👥 Authors

Created for Test et Qualité Logiciel module  
**Project**: The Golden Fork  
**Framework**: .NET (Backend) + Blazor (Frontend)  
**Test Suite**: Selenium + pytest

## 📄 License

This test suite is created for educational purposes as part of the ISTQB project requirements.

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Status**: ✅ Ready for Execution
