from selenium.webdriver.common.by import By

from app.page_object.forms.iframe import IFrame
from framework.elements.button import Button


class EditTextForm:
    def __init__(self):
        self.__iframe = IFrame()

    def select_all_text(self):
        self.edit_button.click()
        self.select_all_button.wait_and_click()

    def click_on_bold(self):
        self.bold_button.click()

    @property
    def iframe(self):
        return self.__iframe

    @property
    def bold_button(self):
        return Button(By.CSS_SELECTOR, ".mce-i-bold", "Button to make text bold")

    @property
    def edit_button(self):
        return Button(By.ID, "mceu_16-open", "Edit text button")

    @property
    def select_all_button(self):
        return Button(By.ID, "mceu_39-text", "Select all text button")
