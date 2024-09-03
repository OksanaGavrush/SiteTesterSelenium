import pytest

from SiteTesterSelenium.tests.data import search_data_for_tests


@pytest.mark.smoke
def test_user_follow_functionality(home_page, user_page, search_page, setup):
    home_page.open()
    search_page.search_for_images(search_data_for_tests.search_images_words_different_format)
    user_page.navigate_to_users_page()
    user_page.select_random_user_profile()
    user_page.follow_user()
    user_page.verify_following_status()


@pytest.mark.regression
def test_email_delivery(home_page, user_page, search_page, setup):
    home_page.open()
    search_page.search_for_images(search_data_for_tests.search_images_words_different_format)
    user_page.navigate_to_users_page()
    user_page.select_random_user_profile()
    user_page.click_message_button()
    user_page.enter_message_in_textarea(search_data_for_tests.message)
    user_page.verify_message_length()
