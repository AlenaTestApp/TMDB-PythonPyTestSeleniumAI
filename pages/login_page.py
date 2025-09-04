"""PAGES CLASSES"""


from pages.locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*LoginLocators.LOGIN_HOMEPAGE).click()
        self.driver.find_element(*LoginLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def check_profile_name(self):
        avatar_name = self.driver.find_element(*LoginLocators.AVATAR_NAME).text
        return avatar_name

    def check_login_error(self, username, password):
        self.login(username, password)
        error_msg = self.driver.find_element(*LoginLocators.LOGIN_ERROR).text
        return error_msg
