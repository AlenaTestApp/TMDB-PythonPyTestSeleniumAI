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


# Artist Page Locators

class ArtistLocators:
    PEOPLE = (By.XPATH, '//a[contains(text(), "People")]')
    POPULAR_PEOPLE = (By.XPATH, '//a[contains(text(), "Popular People")]')
    SEARCH_ICON = (By.XPATH, '//li[contains(@class, "search_buttons")]/a[1]')
    ARTIST_SEARCH = (By.NAME, 'query')
    ART_PROFILE = lambda artist: (By.XPATH, f"//a[contains(text(), '{artist}')]")
    MEDIA_BTN = (By.XPATH, "//div[@id = 'shortcut_bar_scroller']//span[contains(normalize-space(.), 'Media')]")
    MEDIA_PROFILE = (By.CSS_SELECTOR, "a[href*='/images/profiles']")
    PROFILE_IMAGES = (By.XPATH, "//ul[contains(@class, 'images')]/li//img")