"""Test Login Functionality"""


from pages.login_page import LoginPage
from configs.credentials import *


def test_login_valid_credentials(login_page):
    """Test Login Functionality with valid credentials"""
    login_page.login(USER_NAME, USER_PWD)
    assert login_page.check_profile_name() == USER_NAME


def test_login_invalid_credentials(login_page):
    """Test Login Functionality with not registered User"""
    assert LOGIN_ERROR_MSG in login_page.check_login_error(NOT_REGISTERED_USER, USER_PWD)

