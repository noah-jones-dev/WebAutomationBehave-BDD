from framework.fields.element_base import ElementBase
from selenium.webdriver.common.keys import Keys
from framework.helpers.verifications.verify_text import VerifyText

class TextField(ElementBase):
    
    def enter(self, text: str):
        """Enters text into the text field."""
        element = self.element()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)
        
    @property
    def verify(self) -> VerifyText:
        """Returns a verifications object for this text field."""
        return VerifyText(self)

    
    
