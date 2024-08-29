import allure
import random
import string
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SiteTesterSelenium.pages.base_page import BasePage
from SiteTesterSelenium.pages.locators.locators import ProfilePageLocators as loc


class ProfilePage(BasePage):
    relative_url = '/@doe69059'

    @staticmethod
    def generate_random_name(length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step("Navigate to account page")
    def navigate_to_account_page(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.PERSONAL_MENU_BUTTON)).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.VIEW_PROFILE_LINK)).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.ACCOUNT_LINK)).click()

    @allure.step("Update first name with a random value")
    def update_first_name(self):
        new_name = self.generate_random_name()
        first_name_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.FIRST_NAME_FIELD))
        first_name_field.clear()
        first_name_field.send_keys(new_name)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.find(loc.UPDATE_ACCOUNT_BUTTON).click()
        return new_name

    @allure.step("Verify updated first name")
    def verify_updated_first_name(self, expected_name):
        updated_name = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.FIRST_NAME_FIELD)
        ).get_attribute('value')
        assert updated_name == expected_name, f"Expected first name to be {expected_name}, but got {updated_name}"

    @allure.step("Update last name with a long string and verify input length")
    def update_last_name_with_long_string(self, max_length):
        last_name_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.LAST_NAME_FIELD))
        last_name_field.clear()
        test_string = "a" * (max_length + 1)
        last_name_field.send_keys(test_string)
        entered_value = last_name_field.get_attribute('value')
        self.find(loc.UPDATE_ACCOUNT_BUTTON).click()
        assert len(entered_value) == len(test_string), \
            "The input length does not match the expected length, which might indicate a max length limit."

    @allure.step("Update email with an invalid value and verify URL does not change")
    def update_email_with_invalid_value(self, save_cookies_func):
        email_input = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys("invalid-email")
        initial_url = self.driver.current_url
        self.find(loc.UPDATE_ACCOUNT_BUTTON).click()
        save_cookies_func(self.driver)
        assert self.driver.current_url == initial_url, "URL should not change after submitting an invalid email"

    @allure.step("Toggle 'Allow Messages' checkbox and verify state change")
    def toggle_allow_messages_checkbox(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.ALLOW_MESSAGES_CHECKBOX))
        is_checked_initially = checkbox.is_selected()
        checkbox.click()
        WebDriverWait(self.driver, 10).until(lambda driver: checkbox.is_selected() != is_checked_initially,
                                             message="Checkbox state did not change after click.")
        is_checked_after_click = checkbox.is_selected()
        assert is_checked_after_click != is_checked_initially, "Checkbox did not toggle its state."

    @allure.step("Update username with an invalid value and verify form error")
    def update_username_with_invalid_value(self, value):
        user_username_input = self.find(loc.USER_USERNAME_INPUT)
        user_username_input.clear()
        user_username_input.send_keys(value)
        self.driver.execute_script("window.scrollBy(0, 1500);")
        self.find(loc.UPDATE_ACCOUNT_BUTTON).click()
        form_error = self.find(loc.FORM_ERROR)
        assert 'Username must have at least one letter' in form_error.text

    @allure.step("Upload a random new image")
    def upload_random_image(self):
        image_paths = [
            "/Users/oksana/qa/Project_selenium/SiteTesterSelenium/images/cat.jpg",
            "/Users/oksana/qa/Project_selenium/SiteTesterSelenium/images/photo.jpg",
            "/Users/oksana/qa/Project_selenium/SiteTesterSelenium/images/smile.jpg"
        ]
        new_image_path = random.choice(image_paths)
        self.find(loc.PROFILE_IMAGE_CHANGE_LINK).click()
        file_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(loc.FILE_INPUT))
        file_input.send_keys(new_image_path)

    @allure.step("Wait for image upload to complete")
    def wait_for_image_upload(self):
        WebDriverWait(self.driver, 15).until(
            ec.text_to_be_present_in_element(loc.CHANGE_PROFILE_IMAGE_TEXT, "Change profile image"))

    @allure.step("Click submit button")
    def click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable(loc.SUBMIT_BUTTON))
        submit_button.click()

    @allure.step("Verify new profile image is displayed")
    def verify_new_image_displayed(self):
        new_image = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(loc.NEW_IMAGE_SELECTOR))
        assert new_image.get_attribute('src'), "Image did not load."
        assert new_image.is_displayed(), "Image is not displayed on the page."

    @allure.step('Upload image larger than allowed size')
    def upload_image_exceeds_size_limit(self):
        image_path = "/Users/oksana/qa/Project_selenium/SiteTesterSelenium/images/nathan.jpg"
        self.find(loc.CHANGE_PROFILE_IMAGE_TEXT).click()
        file_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(loc.FILE_INPUT_SELECTOR))
        file_input.send_keys(image_path)
        error_message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.ERROR_MESSAGE_SELECTOR))
        assert (
                    "Profile image must be less than 1MB. Try reducing the size of image." in error_message.text),\
            "Error message not displayed or incorrect."

    @allure.step("Add hobbies as tags")
    def add_hobbies(self, hobbies):
        tag_input_field = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(loc.TAG_INPUT_FIELD_SELECTOR))
        for hobby in hobbies:
            tag_input_field.send_keys(hobby)
            tag_input_field.send_keys(Keys.ENTER)

    @allure.step("Verify the input field is displayed and initially valid")
    def verify_input_field(self):
        input_field = self.find(loc.TAG_INPUT_FIELD_SELECTOR)
        assert input_field.is_displayed(), "Input field is not displayed."
        assert 'ui-autocomplete-input not_valid' not in input_field.get_attribute('class'), \
            "Field should not be marked as invalid initially."

    @allure.step("Wait for 'Update account' button to be clickable and click it")
    def wait_and_click_update_account_button(self):
        update_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.UPDATE_ACCOUNT_BUTTON))
        update_button.click()

    @allure.step("Verify the number of added tags")
    def verify_number_of_added_tags(self, nuber):
        added_tags = self.driver.find_elements(*loc.TAG_SPAN_SELECTOR)
        assert len(added_tags) == nuber, f"More than {nuber} tags were added, which should not be possible."

    @allure.step("Remove five tags from user interests")
    def remove_five_tags(self):
        for i in range(5):
            removing_tag = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(loc.REMOVING_TAG_SELECTOR))
            removing_tag.click()
            WebDriverWait(self.driver, 2).until(ec.staleness_of(removing_tag))

    @allure.step("Verify the tag input field is marked as invalid for duplicate tags")
    def verify_tag_input_field_invalid_for_duplicates(self):
        input_field = self.find(loc.TAG_INPUT_FIELD_SELECTOR)
        assert input_field.is_displayed(), "Input field is not displayed."
        assert 'not_valid' in input_field.get_attribute('class'), \
            "Field should be marked as invalid for duplicate tags."

    @allure.step("Set user location with a specific length")
    def set_user_location(self, location):
        user_location = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.USER_LOCATION_SELECTOR))
        user_location.clear()
        user_location.send_keys(location)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))).click()
        check_len_location = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.USER_LOCATION_SELECTOR))
        actual_value = check_len_location.get_attribute('value')
        assert len(actual_value) == 255, f"Expected length of 255, but got {len(actual_value)}"

    @allure.step("Verify the location input field contains the correct value")
    def verify_location_value(self, expected_value):
        check_len_location = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.USER_LOCATION_SELECTOR))
        check_len_location.clear()
        check_len_location.send_keys(expected_value)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.SUBMIT_BUTTON)).click()
        self.driver.refresh()
        updated_location = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.USER_LOCATION_SELECTOR))
        new_location_value = updated_location.get_attribute('value')
        assert new_location_value == "New York", f"Expected location to be 'New York', but got '{new_location_value}'"

    @allure.step("Wait for the 'Likes' link to be clickable and click it")
    def click_likes_link(self):

        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.LIKES_LINK_SELECTOR)).click()

    @allure.step("Get the current count of liked images")
    def get_liked_images_count(self):
        return len(WebDriverWait(self.driver, 10).until(
            ec.visibility_of_all_elements_located(loc.CONTENT_URL_SELECTOR)))

    @allure.step("Unlike a random image")
    def unlike_random_image(self):
        images = self.driver.find_elements(*loc.CONTENT_URL_SELECTOR)
        random_index = random.randint(0, len(images) - 1)
        unlike_buttons = self.driver.find_elements(*loc.UNLIKE_BUTTON_SELECTOR)
        action = ActionChains(self.driver)
        action.move_to_element(unlike_buttons[random_index]).click().perform()

    @allure.step("Refresh the page and verify the image count decreased")
    def verify_image_count_decreased(self, initial_count):
        self.driver.refresh()
        final_count = len(self.driver.find_elements(*loc.CONTENT_URL_SELECTOR))
        assert final_count == initial_count - 1, "The photo count did not decrease as expected."

    @allure.step("Test maximum character limit in the bio textarea")
    def verify_bio_textarea_character_limit(self):
        textarea = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.BIO_TEXTAREA_SELECTOR))
        find_max_len = self.find(loc.BIO_TEXTAREA_SELECTOR)
        max_chars = int(find_max_len.get_attribute('data-character-count'))
        input_text = 'A' * (max_chars + 50)
        textarea.send_keys(input_text)
        error_div = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(loc.CHARACTER_COUNT_ERROR_DIV))
        assert error_div is not None, "Error class was not added to the character count div."

    @allure.step("Clicking on user navigation link for collections")
    def click_user_nav_link(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.USER_NAV_LINK_COLLECTIONS_SELECTOR)).click()

    @allure.step("Fetching list of collections")
    def get_collections(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(loc.COLLECTION_FEED_CARD_SELECTOR))
        return self.driver.find_elements(*loc.COLLECTION_FEED_CARD_SELECTOR)

    @allure.step("Clicking on a random collection")
    def click_random_collection(self, collections):
        random_index = random.randint(0, len(collections) - 1)
        random_image = collections[random_index]
        actions = ActionChains(self.driver)
        actions.move_to_element(random_image).click().perform()

    @allure.step("Deleting a collection")
    def delete_collection(self, collections_before):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.EDIT_COLLECTION_BUTTON_SELECTOR)).click()
        self.driver.find_element(*loc.DELETE_COLLECTION_BUTTON_SELECTOR).click()
        self.driver.find_element(*loc.CONFIRM_DELETE_BUTTON_SELECTOR).click()
        collections_after_delete = self.get_collections()
        assert len(collections_before) > len(collections_after_delete), "Collection was not deleted"
