from framework.fields.element_base import ElementBase
from selenium.webdriver.support import expected_conditions as EC
from framework.helpers.verifications.verify_list import VerifyList

class ListField(ElementBase):

    def get_items(self):
        """Returns a list of items in the list field."""
        elements = self.elements()
        return [element.text for element in elements]

    def select_item(self, item_text):
        """Selects an item from the list by its text."""
        elements = self.elements()
        for element in elements:
            if item_text in element.text:
                self.scroll_to(element)
                element.click()
                return
        raise ValueError(f"Item '{item_text}' not found in the list.")
    
    @property
    def verify(self) -> VerifyList:
        """Returns a verifications object for this list field."""
        return VerifyList(self)