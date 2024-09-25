import random

import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from SiteTesterSelenium.pages.base_page import BasePage
from SiteTesterSelenium.pages.locators.locators import UserPageLocators as loc


class UserPage(BasePage):

    @allure.step("Navigate to the 'Users' page")
    def navigate_to_users_page(self):
        users_link = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.USERS_LINK))
        users_link.click()

    @allure.step("Select a random user profile")
    def select_random_user_profile(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(loc.VIEW_PROFILE_LINKS))
        profile_links = self.driver.find_elements(*loc.VIEW_PROFILE_LINKS)
        random.choice(profile_links).click()

    @allure.step("Follow the selected user")
    def follow_user(self):
        follow_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.FOLLOW_BUTTON))
        follow_button.click()
        click_follow = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.MENU_ITEM))
        click_follow.click()
        if 'Follow' in click_follow.text:
            click_follow.click()
        elif 'Unfollow' in click_follow.text:
            pass
        else:
            print("The button status is unknown.")

    @allure.step("Verify that the user is followed")
    def verify_following_status(self):
        click_follow = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.MENU_ITEM))
        assert 'Unfollow' in click_follow.text, "The button should show 'Unfollow' after following."

    @allure.step("Click the 'Message' button")
    def click_message_button(self):
        message_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.MESSAGE_BUTTON))
        message_button.click()

    @allure.step("Enter a message in the textarea")
    def enter_message_in_textarea(self, message):
        textarea_element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.TEXTAREA))
        textarea_element.click()
        textarea_element.send_keys(message)

    @allure.step("Verify that the entered message does not exceed the maximum length")
    def verify_message_length(self):
        textarea_element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.TEXTAREA))
        entered_text = textarea_element.get_attribute('value')
        max_length = int(textarea_element.get_attribute('maxlength'))
        assert len(entered_text) <= max_length, "Text length exceeds the maximum allowed length."
