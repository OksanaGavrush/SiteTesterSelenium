def test_download_image_by_search(home_page, search_page, photo_page, setup):
    home_page.open()
    files_before = photo_page.prepare_for_search_and_get_files_before()
    search_page.search_for_images('cookies')
    photo_page.filter_by_free_license()
    image, random_index = photo_page.select_random_image()
    photo_page.download_selected_image(image, random_index)
    photo_page.wait_for_download(files_before)


def test_click_add_new_collection(home_page, search_page, photo_page, setup):
    home_page.open()
    search_page.search_for_images('cookies')
    photo_page.filter_by_free_license()
    image, random_index = photo_page.wait_for_images_and_select_random()
    photo_page.add_image_to_collection(image, random_index)
    collection_name = photo_page.create_new_collection()
    photo_page.verify_collection_created(collection_name)


def test_show_more_images(home_page, search_page, photo_page, setup):
    home_page.open()
    search_page.search_for_images('cookies')
    photo_page.filter_by_free_license()
    photo_page.click_load_more_and_verify_count()


def test_verify_collection_button_url(home_page, photo_page, search_page, setup):
    home_page.open()
    search_page.search_for_images('cookies')
    photo_page.verify_collection_link_redirect()


def test_filter_and_display_images_in_different_format(home_page, photo_page, search_page, setup):
    home_page.open()
    search_page.search_for_images('chips')
    photo_page.filter_by_free_license()
    photo_page.select_free_option_and_verify_url()


def test_link_pinterest(home_page, photo_page, setup):
    home_page.open()
    photo_page.wait_for_images_select_and_click()
    photo_page.share_on_pinterest()







