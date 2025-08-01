from framework.fields.element_base import ElementBase
from framework.helpers.verifications.verify_button import VerifyButton

class ButtonField(ElementBase):
    
    @property
    def verify(self) -> VerifyButton:
        """Returns a verifications object for this button field."""
        return VerifyButton(self)
