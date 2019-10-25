from selenium.webdriver.common.by import By

from app.page_object.pages.iframe_page import IFramePage
from framework.browser.browser import Browser
from framework.utils.cloudinary_utils import get_link_to_download_from_cloudinary
from framework.utils.comparison_utils import compare_two_images
from framework.utils.download_utils import download_file
from framework.utils.logger import info
from resources import config

browser = Browser()
iframe_page = IFramePage(By.XPATH, "//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']")
IFRAME_LOC = "mce_0_ifr"


def clear_form_and_enter_text(text):
    browser.switch_to_frame(By.ID, IFRAME_LOC)
    iframe_page.edit_text_form.iframe.clear_form()
    iframe_page.edit_text_form.iframe.enter_text(text)


def check_for_text_entered(text):
    info("Checking that text was entered")
    assert iframe_page.edit_text_form.iframe.is_text_entered(text), "Text wasn't entered"
    browser.switch_to_default_content()


def check_for_text_turned_to_bold(text):
    info("Checking for text turned to bold")
    browser.switch_to_frame(By.ID, IFRAME_LOC)
    assert iframe_page.edit_text_form.iframe.is_text_entered(text), "Text wasn't turned to bold"


def check_that_images_are_same(photo_public_id):
    download_file(get_link_to_download_from_cloudinary(photo_public_id), config.PATH_TO_DOWNLOAD_PICTURE)
    assert compare_two_images(config.PATH_TO_DOWNLOAD_PICTURE,
                              config.PATH_TO_SAVE_SCREENSHOT), "Images are not the same"
