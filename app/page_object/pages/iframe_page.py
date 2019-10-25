from app.page_object.forms.edit_text_form import EditTextForm
from framework.base.base_page import BasePage


class IFramePage(BasePage):
    def __init__(self, locator_type, locator):
        super().__init__(locator_type, locator)
        self.__edit_text_form = EditTextForm()

    @property
    def edit_text_form(self):
        return self.__edit_text_form
