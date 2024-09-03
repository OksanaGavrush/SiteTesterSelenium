import os
import pytest
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from SiteTesterSelenium.pages.home_page import HomePage
from SiteTesterSelenium.pages.photos_page import PhotoPage
from SiteTesterSelenium.pages.profile_page import ProfilePage
from SiteTesterSelenium.pages.search_page import SearchPage
from SiteTesterSelenium.pages.user_page import UserPage
from dotenv import load_dotenv
import os


load_dotenv()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def save_cookies(driver, path='cookies.pkl'):
    with open(path, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)


def load_cookies(driver, path='cookies.pkl'):
    with open(path, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
            driver.add_cookie(cookie)


@pytest.fixture
def setup(driver):
    driver.get('https://unsplash.com/login?referrer=%2F')
    if os.path.exists('cookies.pkl'):
        load_cookies(driver)
        driver.refresh()

    else:
        driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(os.getenv("EMAIL"))
        driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(os.getenv("PASSWORD"))
        driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()
        save_cookies(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def search_page(driver):
    return SearchPage(driver)


@pytest.fixture()
def photo_page(driver):
    return PhotoPage(driver)


@pytest.fixture()
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture()
def user_page(driver):
    return UserPage(driver)
