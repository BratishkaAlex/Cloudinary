from selenium.webdriver.common.by import By

from app.page_object.forms.edit_text_form import EditTextForm
from framework.base.base_page import BasePage


class IFramePage(BasePage):
    def __init__(self):
        super().__init__(By.XPATH, "//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']")
        self.__edit_text_form = EditTextForm()

    @property
    def edit_text_form(self):
        return self.__edit_text_form
