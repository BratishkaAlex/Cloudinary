import os

from app.steps.steps import *
from framework.browser.browser import Browser
from framework.utils.cloudinary_utils import cloudinary_authorize, cloudinary_upload_file, \
    get_link_to_download_from_cloudinary
from framework.utils.comparison_utils import check_that_images_are_equal
from framework.utils.download_utils import download_file
from framework.utils.logger import step
from framework.utils.random_utils import get_random_string
from resources import config


class TestIFrame:
    counter = 1
    browser = Browser()

    def setup_method(self):
        if os.path.exists(config.PATH_TO_DOWNLOAD_PICTURE):
            os.remove(config.PATH_TO_DOWNLOAD_PICTURE)
        if os.path.exists(config.PATH_TO_SAVE_SCREENSHOT):
            os.remove(config.PATH_TO_SAVE_SCREENSHOT)
        cloudinary_authorize()
        self.browser.maximize()
        self.browser.set_implicitly_wait(config.TIMEOUT)

    def teardown_method(self):
        self.browser.close()

    def test_iframe(self):
        step(f"Go to {config.URL}", self.counter)
        self.counter += 1
        self.browser.enter_url(config.URL)
        i_frame_page = IFramePage()
        assert i_frame_page.is_page_opened(), "Page wasn't opened"

        step("Clear input field and enter random line", self.counter)
        self.counter += 1
        random_string = get_random_string()
        clear_form_and_enter_text(random_string)
        check_for_text_entered(random_string)

        step("Select all text and click 'B' button", self.counter)
        self.counter += 1
        i_frame_page.edit_text_form.select_all_text()
        i_frame_page.edit_text_form.click_on_bold()
        check_for_text_turned_to_bold(random_string)

        step("Make screenshot", self.counter)
        self.counter += 1
        browser.save_screenshot(config.PATH_TO_SAVE_SCREENSHOT)

        step("Upload screenshot on cloudinary", self.counter)
        self.counter += 1
        photo_public_id = get_random_string()
        cloudinary_upload_file(config.PATH_TO_SAVE_SCREENSHOT, photo_public_id)

        step("Check that two images are same", self.counter)
        download_file(get_link_to_download_from_cloudinary(photo_public_id), config.PATH_TO_DOWNLOAD_PICTURE)
        assert check_that_images_are_equal(config.PATH_TO_DOWNLOAD_PICTURE,
                                           config.PATH_TO_SAVE_SCREENSHOT), "Images are not the same"
