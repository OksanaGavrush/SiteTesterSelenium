import os
import pytest
import pickle
from selenium.webdriver.common.by import By


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
        email = os.getenv("EMAIL", "")
        password = os.getenv("PASSWORD", "")
        driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(email)
        driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()
        save_cookies(driver)