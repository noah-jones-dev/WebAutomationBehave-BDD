from framework.helpers.verifications.verify_base import VerifyBase

class VerifyList(VerifyBase):
    
    
    def item_exists(self, item: str):
        """Verify that the specified item exists in the list."""
        elements = self.element_base.elements()
        items = elements.get_items()
        assert item in items, f"Item '{item}' does not exist in the list."

    def item_not_exists(self, item: str):
        """Verify that the specified item does not exist in the list."""
        elements = self.element_base.elements()
        items = elements.get_items()
        assert item not in items, f"Item '{item}' exists in the list."

    def item_selected(self, item: str):
        """Verify that the specified item is selected in the list."""
        elements = self.element_base.elements()
        items = elements.get_items()
        for element in elements:
            if element.text == item:
                assert element.is_selected(), f"Item '{item}' is not selected in the list."
        assert item in items, f"Item '{item}' is not selected in the list."
        
    def size_is_greater(self, size: int):
        """Verify that the size of the list is greater than the expected size."""
        elements = self.element_base.elements()
        current_size = len(elements)
        assert current_size > size, f"Expected size greater than {size} but got {current_size}."
