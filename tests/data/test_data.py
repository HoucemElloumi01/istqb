"""
Test data generators and constants
Provides test data for various test scenarios
"""
from faker import Faker
import random
import string

fake = Faker()


class TestData:
    """Test data generator class"""
    
    @staticmethod
    def generate_random_email():
        """Generate random email address"""
        return fake.email()
    
    @staticmethod
    def generate_random_username():
        """Generate random username"""
        return fake.user_name()
    
    @staticmethod
    def generate_random_phone():
        """Generate random phone number"""
        return fake.phone_number()
    
    @staticmethod
    def generate_strong_password():
        """Generate strong password"""
        return fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    @staticmethod
    def generate_weak_password():
        """Generate weak password (too short)"""
        return ''.join(random.choices(string.ascii_lowercase, k=4))
    
    @staticmethod
    def generate_random_text(length=50):
        """Generate random text"""
        return fake.text(max_nb_chars=length)
    
    @staticmethod
    def generate_menu_name():
        """Generate menu name"""
        menu_types = ["Breakfast", "Lunch", "Dinner", "Desserts", "Beverages", "Special", "Weekend", "Seasonal"]
        return f"{random.choice(menu_types)} Menu {random.randint(1, 100)}"
    
    @staticmethod
    def generate_menu_description():
        """Generate menu description"""
        return fake.text(max_nb_chars=100)


# Valid test credentials
VALID_USER = {
    "email": "testuser@goldenfork.com",
    "password": "TestPass123!",
    "username": "testuser",
    "phone": "+216 98 123 456"
}

VALID_ADMIN = {
    "email": "admin@goldenfork.com",
    "password": "AdminPass123!",
    "username": "adminuser",
    "phone": "+216 98 987 654"
}

# Invalid test data - Equivalence Partitioning
INVALID_EMAILS = [
    "",  # Empty
    "notanemail",  # No @ symbol
    "@example.com",  # No local part
    "user@",  # No domain
    "user @example.com",  # Space in email
    "user@.com",  # Invalid domain
]

INVALID_PASSWORDS = [
    "",  # Empty
    "123",  # Too short (< 6 chars)
    "12345",  # Too short (< 6 chars)
    "     ",  # Only spaces
]

# Boundary value test data
BOUNDARY_VALUES = {
    "username_min": "abc",  # Minimum 3 characters
    "username_max": "a" * 50,  # Maximum 50 characters
    "username_below_min": "ab",  # Below minimum
    "username_above_max": "a" * 51,  # Above maximum
    "password_min": "pass12",  # Minimum 6 characters
    "password_below_min": "pas12",  # Below minimum (5 chars)
}

# Test menus data
TEST_MENUS = [
    {
        "name": "Breakfast Special",
        "description": "Start your day with our delicious breakfast options"
    },
    {
        "name": "Lunch Combo",
        "description": "Perfect midday meals with great value"
    },
    {
        "name": "Dinner Delights",
        "description": "Exquisite dinner selections for a memorable evening"
    }
]

# Test categories data
TEST_CATEGORIES = [
    {"name": "Appetizers", "description": "Start your meal right"},
    {"name": "Main Course", "description": "Hearty main dishes"},
    {"name": "Desserts", "description": "Sweet endings"}
]

# Test items data
TEST_ITEMS = [
    {
        "name": "Golden Burger",
        "description": "Premium beef burger with special sauce",
        "price": 12.99
    },
    {
        "name": "Caesar Salad",
        "description": "Fresh romaine with parmesan and croutons",
        "price": 8.99
    },
    {
        "name": "Chocolate Cake",
        "description": "Rich chocolate cake with ganache",
        "price": 6.99
    }
]
