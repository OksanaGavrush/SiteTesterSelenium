import pytest
from SiteTesterSelenium.conftest import save_cookies
from SiteTesterSelenium.tests.data import search_data_for_tests


@pytest.mark.regression
def test_update_email_with_invalid_value(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)


@pytest.mark.regression
def test_update_user_name_profile(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    new_name = profile_page.update_first_name()
    profile_page.verify_updated_first_name(new_name)


@pytest.mark.regression
def test_max_length_user_last_name(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    profile_page.update_last_name_with_long_string(search_data_for_tests.max_length)


@pytest.mark.smoke
def test_display_message_button_on_profile(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.toggle_allow_messages_checkbox()


@pytest.mark.regression
def test_update_username_with_invalid_value(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_username_with_invalid_value(search_data_for_tests.invalid_value)


@pytest.mark.regression
def test_profile_image_upload(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.upload_random_image()
    profile_page.wait_for_image_upload()
    profile_page.click_submit_button()
    profile_page.verify_new_image_displayed()


@pytest.mark.regression
def test_profile_image_upload_exceeds_size_limit(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.upload_image_exceeds_size_limit()


@pytest.mark.regression
def test_interests_tags_input(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.add_hobbies(search_data_for_tests.hobbies)
    profile_page.wait_and_click_update_account_button()
    profile_page.verify_number_of_added_tags(5)
    profile_page.wait_and_click_update_account_button()


@pytest.mark.regression
def test_no_duplicate_interests(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    profile_page.remove_five_tags()
    profile_page.add_hobbies(search_data_for_tests.duplicate_hobbies)
    profile_page.verify_tag_input_field_invalid_for_duplicates()


@pytest.mark.regression
def test_location_input_length_boundaries(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    profile_page.set_user_location(search_data_for_tests.input_length)
    profile_page.verify_location_value(search_data_for_tests.location_value)


@pytest.mark.regression
def test_unlike_image(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    profile_page.click_likes_link()
    initial_count = profile_page.get_liked_images_count()
    profile_page.unlike_random_image()
    profile_page.verify_image_count_decreased(initial_count)


@pytest.mark.regression
def test_character_count_limit(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.verify_bio_textarea_character_limit()


@pytest.mark.regression
def test_delete_photo_collection(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    profile_page.click_user_nav_link()
    collections = profile_page.get_collections()
    profile_page.click_random_collection(collections)
    profile_page.delete_collection(collections)
