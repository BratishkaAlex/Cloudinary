from framework.browser.browser_factory import get_driver
from framework.models.singleton import Singleton
from framework.utils.logger import debug
from resources import config


class Browser(metaclass=Singleton):
    def __init__(self):
        self.__driver = get_driver()

    @property
    def driver(self):
        return self.__driver

    def maximize(self):
        debug("Maximize browser window")
        self.driver.maximize_window()

    def enter_url(self, url):
        debug(f"Entering {url}")
        self.driver.get(url)

    def close(self):
        debug("Close browser")
        self.driver.close()

    def set_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def get_current_url(self):
        debug("Get current browser")
        return self.driver.current_url

    def switch_to_frame(self, by, loc):
        debug("Change focus on iframe")
        self.driver.switch_to_frame(self.driver.find_element(by, loc))

    def switch_to_default_content(self):
        debug("Change focus on default content")
        self.driver.switch_to_default_content()

    def save_screenshot(self):
        debug("Make screenshot")
        self.driver.get_screenshot_as_file(config.PATH_TO_SAVE_SCREENSHOT)
