import pytest
from SiteTesterSelenium.tests.data import search_data_for_tests


@pytest.mark.smoke
def test_search_input_functionality(home_page, search_page, setup):
    home_page.open()
    home_page.search(search_data_for_tests.search_input)
    search_page.verify_results()
    search_page.verify_url(search_data_for_tests.search_input)


@pytest.mark.smoke
def test_click_random_heart_icon(home_page, setup):
    home_page.open()
    home_page.clicking_random_image()
    home_page.like_the_image()


@pytest.mark.smoke
def test_link_copy_check(home_page, setup):
    home_page.open()
    home_page.clicking_random_image()
    home_page.click_share_button()


@pytest.mark.smoke
def test_burger_menu_opens(home_page, setup):
    home_page.open()
    home_page.wait_for_burger_menu()
    home_page.click_burger_menu()
    home_page.verify_burger_menu_opened()


@pytest.mark.smoke
def test_language_selection(home_page, setup):
    home_page.open()
    home_page.wait_for_burger_menu()
    home_page.click_burger_menu()
    home_page.select_language()
    home_page.verify_language_change(search_data_for_tests.search_language_text)


@pytest.mark.smoke
def test_scroll_right_button(home_page, setup):
    home_page.open()
    home_page.scroll_right_button()
    home_page.verify_scroll_left_button()


@pytest.mark.smoke
def test_scroll_left_button(home_page, setup):
    home_page.open()
    home_page.scroll_right_button()
    home_page.scroll_left_button()


@pytest.mark.smoke
def test_upgrade_to_unsplash_plus(home_page, search_page, setup):
    home_page.open()
    search_page.check_button_to_upgrade()


@pytest.mark.smoke
def test_view_notifications(home_page, setup):
    home_page.open()
    home_page.open_notifications()
    home_page.click_highlights_button()
