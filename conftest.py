import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SiteTesterSelenium.pages.home_page import HomePage
from SiteTesterSelenium.pages.photos_page import PhotoPage
from SiteTesterSelenium.pages.profile_page import ProfilePage
from SiteTesterSelenium.pages.search_page import SearchPage
from SiteTesterSelenium.pages.user_page import UserPage
from dotenv import load_dotenv


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
