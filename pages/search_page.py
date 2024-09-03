import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SiteTesterSelenium.pages.base_page import BasePage
from SiteTesterSelenium.pages.locators.locators import SearchPageLocators as loc


class SearchPage(BasePage):

    @allure.step("Verify search results are displayed")
    def verify_results(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, 'img')
        assert len(results) > 0, "No search results found."

    @allure.step("Verify search query is reflected in the URL")
    def verify_url(self, query):
        assert query in self.driver.current_url, "Search query not reflected in the URL."

    @allure.step("Search for images with term '{search_term}'")
    def search_for_images(self, search_term):
        self.driver.maximize_window()
        search_input = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.SEARCH_INPUT))
        search_input.click()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Check button to upgrade subscription")
    def check_button_to_upgrade(self):
        self.find(loc.GET_UNSPLASH).click()
        assert self.driver.current_url == 'https://unsplash.com/plus'
