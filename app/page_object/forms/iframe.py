from selenium.webdriver.common.by import By

from framework.elements.input_field import InputField
from framework.elements.label import Label


class IFrame:
    def clear_form(self):
        self.input_field.clear()

    def enter_text(self, text):
        self.input_field.send_keys(text)

    def is_text_entered(self, text):
        return self.input_field.get_text() == text

    def is_test_turned_to_bold(self, text):
        return self.get_bold_text(text).is_displayed()

    @property
    def input_field(self):
        return InputField(By.ID, "tinymce", "Input text form")

    def get_bold_text(self, text):
        return Label(By.XPATH, f"//strong[text()='{text}']", "Strong entered text")
