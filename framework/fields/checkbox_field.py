from framework.fields.element_base import ElementBase
from framework.helpers.verifications.verify_checkbox import VerifyCheckbox

class CheckboxField(ElementBase):
    
    @property
    def verify(self) -> VerifyCheckbox:
        """Returns a verifications object for this checkbox field."""
        return VerifyCheckbox(self)
    
    def check(self):
        element = self.element()
        if not element.is_selected():
            element.click()
            
    def uncheck(self):
        element = self.element()
        if element.is_selected():
            element.click()