"""PAGES LOCATORS"""


from selenium.webdriver.common.by import By


# Home Page Locators
class LoginLocators:
    LOGIN_HOMEPAGE = (By.XPATH, '//a[contains(text(), "Login")]')
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login_button')
    AVATAR_NAME = (By.XPATH, '//div[@class = "about"]//a')
    LOGIN_ERROR = (By.XPATH, '//div[contains(@class, "error_status")]//h2/span')
