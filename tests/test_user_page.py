def test_user_follow_functionality(home_page, user_page, search_page, setup):
    home_page.open()
    search_page.search_for_images('chips')
    user_page.navigate_to_users_page()
    user_page.select_random_user_profile()
    user_page.follow_user()
    user_page.verify_following_status()


def test_email_delivery(home_page, user_page, search_page, setup):
    home_page.open()
    search_page.search_for_images('apple')
    user_page.navigate_to_users_page()
    user_page.select_random_user_profile()
    user_page.click_message_button()
    message = 'Hello!' * 200
    user_page.enter_message_in_textarea(message)
    user_page.verify_message_length()
