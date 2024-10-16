import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from SiteTesterSelenium.pages.base_page import BasePage
from SiteTesterSelenium.pages.locators.locators import HomePageLocators as loc


class HomePage(BasePage):
    relative_url = "/"

    @allure.step("Find and click on the search input")
    def click_search_input(self):
        search_input = self.find(loc.SEARCH_INPUT)
        search_input.click()
        return search_input

    @allure.step("Enter search query and press Enter")
    def search(self, query):
        search_input = self.click_search_input()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Select a random image")
    def clicking_random_image(self):
        images = self.find_all(loc.IMAGES)
        random_index = random.randint(1, len(images))
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(
                (By.XPATH, f'(//figure[@itemprop="image"])[{random_index}]'))
        ).click()

    @allure.step("Like the image")
    def like_the_image(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.LIKE_BUTTON))
        like_button = self.find(loc.LIKE_BUTTON)
        like_button.click()

    @allure.step("Verify the image was successfully liked")
    def verify_like_successful(self):
        button_like = self.find(loc.LIKE_BUTTON_SELECTOR)
        button_unlike = self.find(loc.BUTTON_UNLIKE)
        assert button_like.get_attribute('title') != button_unlike.get_attribute('title'), \
            "The image was not successfully liked."

    @allure.step("Click the share button")
    def click_share_button(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.SHARE_BUTTON_TEXT))
        self.find(loc.SHARE_BUTTON_TEXT).click()

    @allure.step("Verify the link was copied successfully")
    def verify_link_share_button_copied(self):
        copy_link = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.COPY_LINK_BUTTON_TEXT))
        copy_link.click()
        assert copy_link.text == 'Copied!', "The link was not copied successfully."

    @allure.step("Click the burger menu")
    def wait_and_click_burger_menu(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.BURGER_MENU_BUTTON))
        click_burger_button = self.find(loc.BURGER_MENU_BUTTON)
        click_burger_button.click()

    @allure.step("Verify the burger menu is opened")
    def verify_burger_menu_opened(self):
        burger_button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.BURGER_MENU_BUTTON)
        )
        aria_expanded = burger_button.get_attribute('aria-expanded')
        assert aria_expanded == 'true', f"Expected 'aria-expanded' to be 'true', got '{aria_expanded}'"

    @allure.step("Select language")
    def select_language(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.LANGUAGE_SELECTOR)).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(loc.SPANISH_LANGUAGE_OPTION)).click()

    @allure.step("Verify language change")
    def verify_language_change(self, expected_word):
        check_language_change = self.find(loc.CHECK_LANGUAGE_CHANGE)
        assert check_language_change.text == expected_word

    @allure.step("Verify scroll right button is displayed and click it multiple times")
    def scroll_right_button(self):
        for _ in range(5):
            scroll_right_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(loc.SCROLL_RIGHT_BUTTON)
            )
            assert scroll_right_button.is_displayed(), "Scroll right button is not displayed"
            scroll_right_button.click()
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.SCROLL_LEFT_BUTTON))

    @allure.step("Verify scroll left button is displayed")
    def verify_scroll_left_button(self):
        left_button = (WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.SCROLL_LEFT_BUTTON))
        )
        assert left_button.is_displayed(), "Scroll left button is not displayed"

    @allure.step("Verify scroll right button is displayed")
    def scroll_left_button(self):
        scroll_left_button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.SCROLL_LEFT_BUTTON)
        )
        assert scroll_left_button.is_displayed(), "Scroll left button is not displayed"
        scroll_left_button.click()

    @allure.step("Navigate to account page")
    def navigate_to_account_page(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.PERSONAL_MENU_BUTTON)).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.VIEW_PROFILE_LINK)).click()

    @allure.step("Click on 'Account' link")
    def click_account_link(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.ACCOUNT_LINK)).click()

    @allure.step("Open the notifications panel")
    def open_notifications(self):
        click_ring_button = self.find(loc.NOTIFICATIONS_BUTTON)
        click_ring_button.click()

    @allure.step("Click on the 'Highlights' button")
    def click_highlights_button(self):
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.ACTIVITY_BUTTON))
        text_in_activity_button = self.driver.find_element(By.CSS_SELECTOR, '.ANdyZ').text
        assert text_in_activity_button == 'Activity associated with your account will appear here.'
