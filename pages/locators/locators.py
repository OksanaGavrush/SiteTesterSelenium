from selenium.webdriver.common.by import By


class HomePageLocators:
    IMAGES = (By.XPATH, '//figure[@itemprop="image"]')
    HOMEPAGE_URL = 'https://unsplash.com'
    SEARCH_INPUT = (By.XPATH, '(//input[@type="search"])[1]')
    LIKE_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'button[title="Like this image"]')
    LIKE_BUTTON = By.CSS_SELECTOR, '.ztgo2 svg[class="O2bBF"]'
    BUTTON_UNLIKE = (By.CSS_SELECTOR, 'button[title="Unlike this image"]')
    SHARE_BUTTON_TEXT = (By.XPATH, '//span[text()="Share"]')
    COPY_LINK_BUTTON_TEXT = (By.XPATH, "//button[.//span[contains(text(), 'Copy link')]]")
    BURGER_MENU_BUTTON = (By.XPATH, '(//button[@role="button"])[4]')
    LANGUAGE_SELECTOR = (By.CSS_SELECTOR, '[title="Select your language"]')
    SPANISH_LANGUAGE_OPTION = (By.XPATH, '(//*[@lang="es-XM"])[3]')
    CHECK_LANGUAGE_CHANGE = (By.XPATH, '(//*[@class="wuIW2 R6ToQ N68bN"])[1]')
    SCROLL_RIGHT_BUTTON = (By.CSS_SELECTOR, 'button[title="scroll list to the right"]')
    SCROLL_LEFT_BUTTON = (By.CSS_SELECTOR, 'button[title="scroll list to the left"]')
    PERSONAL_MENU_BUTTON = (By.CSS_SELECTOR, 'button[title="Your personal menu button"]')
    VIEW_PROFILE_LINK = (By.XPATH, '//a[contains(text(), "View profile")]')
    ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="https://unsplash.com/account"]')
    HIGHLIGHTS_BUTTON = (By.XPATH, '//button[text()="Highlights"]')
    ACTIVITY_BUTTON = (By.XPATH, '//button[text()= "Activity"]')
    NOTIFICATIONS_BUTTON = (By.CSS_SELECTOR, 'button[title="View my notifications"]')


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, '(//input[@type="search"])[1]')
    RADIO_BUTTON = (By.CSS_SELECTOR, 'input[type="radio"][value="month"]')
    GET_UNSPLASH = (By.XPATH, '//a[text()="Get Unsplash+"]')
    GET_UNSPLASH_PLUS = (By.CSS_SELECTOR, '[data-test="get-unsplash-plus"]')


class ProfilePageLocators:
    PERSONAL_MENU_BUTTON = (By.CSS_SELECTOR, 'button[title="Your personal menu button"]')
    VIEW_PROFILE_LINK = (By.XPATH, '//a[contains(text(), "View profile")]')
    ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="https://unsplash.com/account"]')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#user_first_name')
    UPDATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[value="Update account"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#user_last_name')
    EMAIL_INPUT = (By.ID, "user_email")
    USER_USERNAME_INPUT = (By.CSS_SELECTOR, '#user_username')
    FORM_ERROR = (By.CSS_SELECTOR, '.form-error-inline')
    ALLOW_MESSAGES_CHECKBOX = (By.ID, 'allow-messages-checkbox')
    PROFILE_IMAGE_CHANGE_LINK = (By.XPATH, '//p[text() = "Change profile image"]')
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    CHANGE_PROFILE_IMAGE_TEXT = (By.XPATH, '//p[text() = "Change profile image"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    NEW_IMAGE_SELECTOR = (By.CSS_SELECTOR, "img.upload-circular__image")
    CHANGE_PROFILE_IMAGE = (By.XPATH, '//p[text() = "Change profile image"]')
    FILE_INPUT_SELECTOR = (By.CSS_SELECTOR, "input[type='file']")
    ERROR_MESSAGE_SELECTOR = (
    By.XPATH, '//div[contains(@class, "flash__message") and contains(text(), "image must be")]')
    TAG_INPUT_FIELD_SELECTOR = (By.CSS_SELECTOR, '#user_interests_tag')
    TAG_SPAN_SELECTOR = (By.CSS_SELECTOR, 'span.tag > span')
    REMOVING_TAG_SELECTOR = (By.CSS_SELECTOR, '[title="Removing tag"]')
    USER_LOCATION_SELECTOR = (By.CSS_SELECTOR, "#user_location")
    LIKES_LINK_SELECTOR = (By.CSS_SELECTOR, 'a[data-testid="user-nav-link-likes"][href="/@doe69059/likes"]')
    CONTENT_URL_SELECTOR = (By.CSS_SELECTOR, '[itemprop="contentUrl"]')
    UNLIKE_BUTTON_SELECTOR = (By.XPATH, '//button[@title="Unlike this image"]')
    BIO_TEXTAREA_SELECTOR = (By.CSS_SELECTOR, 'textarea#user_bio')
    BIO_TEXTAREA_USER = (By.CSS_SELECTOR, 'user_bio')
    CHARACTER_COUNT_ERROR_DIV = (By.CSS_SELECTOR, 'div.character-count--error')
    USER_NAV_LINK_COLLECTIONS_SELECTOR = (By.CSS_SELECTOR, '[data-testid="user-nav-link-collections"]')
    COLLECTION_FEED_CARD_SELECTOR = (By.CSS_SELECTOR, '[data-testid="collection-feed-card"]')
    EDIT_COLLECTION_BUTTON_SELECTOR = (By.XPATH, '//button[text()="Edit"]')
    DELETE_COLLECTION_BUTTON_SELECTOR = (By.XPATH, '//button[text()="Delete Collection"]')
    CONFIRM_DELETE_BUTTON_SELECTOR = (By.XPATH, '//button[text()="Delete"]')


class PhotosPageLocators:
    IMAGE_LINKS = (By.XPATH, '//a[@itemprop="contentUrl"]')
    FREE_LICENSE_OPTION = (By.XPATH, "//a[contains(., 'Free')]")
    LICENSE_MENU_BUTTON = (By.XPATH, "//button[contains(., 'License') and .//span[contains(., 'All')]]")
    CREATE_NEW_COLLECTION_BUTTON = (By.XPATH, '//button[text()="Create a new collection"]')
    COLLECTION_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Beautiful photos"]')
    PRIVACY_CHECKBOX = (By.NAME, 'privacy')
    NEW_COLLECTION = (By.XPATH, '//button[text() = "Create collection"]')
    LOAD_MORE_BUTTON = (By.XPATH, '//button[text()="Load more"]')
    COLLECTIONS_LINK = (By.CSS_SELECTOR, 'a[data-testid="search-nav-link-collections"]')
    COLLECTION_FEED_CARD = (By.CSS_SELECTOR, '[data-testid="collection-feed-card"]')
    SHARE_BUTTON = (By.XPATH, '//span[text()="Share"]')
    PINTEREST_SHARE_BUTTON = (By.CSS_SELECTOR, "a[title='Share on Pinterest']")


class UserPageLocators:
    USERS_LINK = (By.XPATH, '//a[text()="Users"]')
    VIEW_PROFILE_LINKS = (By.XPATH, '//a[text()="View profile"]')
    FOLLOW_BUTTON = (By.XPATH, '(//button[@aria-haspopup="true"])[5]')
    MENU_ITEM = (By.CSS_SELECTOR, '[role="menuitem"]')
    MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[title*="Message"]')
    TEXTAREA = (By.CSS_SELECTOR, 'textarea[minlength="20"]')
