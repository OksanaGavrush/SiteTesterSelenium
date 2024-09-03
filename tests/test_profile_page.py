from SiteTesterSelenium.conftest import save_cookies


def test_update_email_with_invalid_value(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)


def test_update_user_name_profile(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    new_name = profile_page.update_first_name()
    profile_page.verify_updated_first_name(new_name)


def test_max_length_user_last_name(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    max_length = 1000
    profile_page.update_last_name_with_long_string(max_length)


def test_display_message_button_on_profile(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.toggle_allow_messages_checkbox()


def test_update_username_with_invalid_value(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_username_with_invalid_value('234.')


def test_profile_image_upload(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.upload_random_image()
    profile_page.wait_for_image_upload()
    profile_page.click_submit_button()
    profile_page.verify_new_image_displayed()


def test_profile_image_upload_exceeds_size_limit(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.upload_image_exceeds_size_limit()


def test_interests_tags_input(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    hobbies = ['Reading', 'Photography', 'Hiking', 'Cooking', 'Painting', 'Cycling', 'Gardening', 'Writing']
    profile_page.add_hobbies(hobbies)
    profile_page.wait_and_click_update_account_button()
    profile_page.verify_number_of_added_tags(5)
    profile_page.wait_and_click_update_account_button()


def test_no_duplicate_interests(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    profile_page.remove_five_tags()
    hobbies = ['Photography', 'Photography']
    profile_page.add_hobbies(hobbies)
    profile_page.verify_tag_input_field_invalid_for_duplicates()


def test_location_input_length_boundaries(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.update_email_with_invalid_value(save_cookies)
    profile_page.set_user_location("L" * 255)
    profile_page.verify_location_value("New York")


def test_unlike_image(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    profile_page.click_likes_link()
    initial_count = profile_page.get_liked_images_count()
    profile_page.unlike_random_image()
    profile_page.verify_image_count_decreased(initial_count)


def test_character_count_limit(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    home_page.click_account_link()
    profile_page.verify_bio_textarea_character_limit()


def test_delete_photo_collection(home_page, profile_page, setup):
    home_page.open()
    home_page.navigate_to_account_page()
    profile_page.click_user_nav_link()
    collections = profile_page.get_collections()
    profile_page.click_random_collection(collections)
    profile_page.delete_collection(collections)
