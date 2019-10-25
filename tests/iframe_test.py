import os

from app.steps.steps import *
from framework.browser.browser import Browser
from framework.utils.cloudinary_utils import cloudinary_authorize, cloudinary_upload_file
from framework.utils.logger import step
from framework.utils.random_utils import get_random_string
from framework.utils.waiter import implicit_wait
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
        implicit_wait(config.TIMEOUT)

    def teardown_method(self):
        self.browser.close()

    def test_iframe(self):
        step(f"Go to {config.URL}", self.counter)
        self.counter += 1
        self.browser.enter_url(config.URL)
        i_frame_page = IFramePage(By.XPATH, "//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']")
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
        browser.save_screenshot()

        step("Upload screenshot on cloudinary", self.counter)
        self.counter += 1
        photo_public_id = get_random_string()
        cloudinary_upload_file(config.PATH_TO_SAVE_SCREENSHOT, photo_public_id)

        step("Check that two images are same", self.counter)
        check_that_images_are_same(photo_public_id)
