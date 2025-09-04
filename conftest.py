"""BROWSER SETUP"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configs.env_settings import *
from pages.login_page import LoginPage
from pages.artist_page import ArtistPage
from configs.credentials import *


@pytest.fixture
def driver():
    options = Options()
    if HEADLESS:
        options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def artist_page(login_page):
    login_page.login(USER_NAME, USER_PWD)
    return ArtistPage(login_page.driver)
