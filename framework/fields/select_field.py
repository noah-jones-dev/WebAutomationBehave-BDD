from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from framework.fields.element_base import ElementBase
from framework.helpers.verifications.verify_select import VerifySelect


class SelectField(ElementBase):
    
    def select_option(self, text: str):
        """Select an option from the select field by visible text."""
        select = Select(self.element())
        select.select_by_visible_text(text)
        return self
    
    @property
    def verify(self) -> VerifySelect:
        """Returns a verifications object for this select field."""
        return VerifySelect(self)
    
    