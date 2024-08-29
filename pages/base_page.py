import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Find element")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Find elements")
    def find_oll(self, locator):
        return self.driver.find_elements(*locator)



