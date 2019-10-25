from selenium.webdriver.common.alert import Alert

from framework.browser.browser import Browser
from framework.utils.logger import info


def get_text_from_modal_window():
    info("Checking modal window message")
    return Alert(Browser().driver).text


def accept_modal_window():
    Alert(Browser().driver).accept()


def send_keys_for_modal_window(text):
    Alert(Browser().driver).send_keys(text)
