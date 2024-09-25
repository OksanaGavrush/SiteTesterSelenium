import os
import random
from datetime import datetime

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from SiteTesterSelenium.pages.base_page import BasePage
from SiteTesterSelenium.pages.locators.locators import PhotosPageLocators as loc


class PhotoPage(BasePage):

    @allure.step("Prepare for search and get files before download")
    def prepare_for_search_and_get_files_before(self):
        self.download_path = "/Users/oksana/Downloads"
        files_before = set(os.listdir(self.download_path))
        return files_before

    @allure.step("Filter images by free license")
    def filter_by_free_license(self):
        menu_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.LICENSE_MENU_BUTTON))
        menu_button.click()
        free_option = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.FREE_LICENSE_OPTION))
        free_option.click()

    @allure.step("Select a random image")
    def select_random_image(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(loc.IMAGE_LINKS))
        images = self.driver.find_elements(*loc.IMAGE_LINKS)
        random_index = random.randint(10, len(images))
        RANDOM_IMAGE = (By.XPATH, f'(//a[@itemprop="contentUrl"])[{random_index}]')
        image = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(RANDOM_IMAGE))
        return image, random_index

    @allure.step("Download the selected image")
    def download_selected_image(self, image, random_index):
        actions = ActionChains(self.driver)
        actions.move_to_element(image).perform()
        RANDOM_IMAGE_DOWNLOAD_BUTTON = (By.XPATH,
                                        f'(//a[@itemprop="contentUrl"])[{random_index}]'
                                        f'//following::a[@data-testid="non-sponsored-photo-download-button"]')
        download_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(RANDOM_IMAGE_DOWNLOAD_BUTTON)
        )
        download_button.click()

    @allure.step("Wait for download to complete")
    def wait_for_download(self, files_before):
        WebDriverWait(self.driver, 30).until(lambda d: set(os.listdir(self.download_path)) != files_before)
        files_after = set(os.listdir(self.download_path))
        downloaded_files = files_after - files_before
        assert downloaded_files, "No new file downloaded."

    @allure.step("Wait for images and select a random one")
    def wait_for_images_and_select_random(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(loc.IMAGE_LINKS))
        self.driver.execute_script("window.scrollBy(0, 500);")
        images = self.driver.find_elements(By.XPATH, '//a[@itemprop="contentUrl"]')
        random_index = random.randint(5, len(images))
        RANDOM_IMAGE = (By.XPATH, f'(//a[@itemprop="contentUrl"])[{random_index}]')
        image = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(RANDOM_IMAGE))
        return image, random_index

    @allure.step("Add image to collection")
    def add_image_to_collection(self, image, random_index):
        CLICK_CREATE = (By.XPATH, f'(//button[@title="Add this image to a collection"])[{random_index}]')
        actions = ActionChains(self.driver)
        actions.move_to_element(image).perform()
        click_create_collection = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CLICK_CREATE))
        click_create_collection.click()

    @allure.step("Create a new collection")
    def create_new_collection(self):
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(loc.CREATE_NEW_COLLECTION_BUTTON)).click()
        unique_name = "Collection " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name_input = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.COLLECTION_NAME_INPUT)
        )
        name_input.send_keys(unique_name)
        privacy_checkbox = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.PRIVACY_CHECKBOX))
        privacy_checkbox.click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(loc.NEW_COLLECTION)).click()
        return unique_name

    @allure.step("Verify the collection '{collection_name}' was created")
    def verify_collection_created(self, collection_name):
        COLLECTION_NAME_SPAN = (By.XPATH, f'//span[text()="{collection_name}"]')
        check_create = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(COLLECTION_NAME_SPAN)
        )
        assert check_create.text == collection_name, "The collection was not created successfully."

    @allure.step("Get the image count")
    def get_image_count(self):
        images = self.driver.find_elements(*loc.IMAGE_LINKS)
        return len(images)

    @allure.step("Scroll and click 'Load more' button, then verify the image count increases")
    def click_load_more_and_verify_count(self):
        self.driver.execute_script(f"window.scrollBy(0, 2800);")
        count_before = self.get_image_count()
        load_more_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.LOAD_MORE_BUTTON)
        )
        load_more_button.click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        WebDriverWait(self.driver, 10).until(lambda driver: self.get_image_count() > count_before)
        count_after = self.get_image_count()
        assert count_after > count_before, "The number of images did not increase after clicking 'Load more'"

    @allure.step("Verify that clicking on 'Collections' link redirects to a URL containing 'collections'")
    def verify_collection_link_redirect(self):
        collection_link = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.COLLECTIONS_LINK))
        collection_link.click()
        WebDriverWait(self.driver, 10).until(ec.url_contains("collections"))
        current_url = self.driver.current_url
        assert "collections" in current_url, "'collections' not found in the URL after clicking the 'Collections' link"
        collections = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(loc.COLLECTION_FEED_CARD)
        )
        assert len(collections) > 0, "No collections found on the page after clicking the 'Collections' link"

    @allure.step("Wait for images and select a random one")
    def wait_for_images_select_and_click(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, '//a[@itemprop="contentUrl"]'))
        )
        images = self.driver.find_elements(*loc.IMAGE_LINKS)
        random_index = random.randint(5, len(images))
        image = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, f'(//a[@itemprop="contentUrl"])[{random_index}]'))
        )
        image.click()

    @allure.step("Click on the 'Free' option and verify the URL contains 'free'")
    def select_free_option_and_verify_url(self):
        assert 'free' in self.driver.current_url, "URL does not contain 'free' after clicking the 'Free' option"

    @allure.step("Click 'Share' and share on Pinterest")
    def share_on_pinterest(self):
        share_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.SHARE_BUTTON)
        )
        share_button.click()
        pinterest_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(loc.PINTEREST_SHARE_BUTTON)
        )
        pinterest_button.click()
        assert 'pinterest' in self.driver.current_url, "The current URL does not contain 'pinterest'"
