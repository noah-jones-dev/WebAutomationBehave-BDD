from framework.helpers.verifications.verify_base import VerifyBase

class VerifyCheckbox(VerifyBase):
    
    def is_checked(self) -> bool:
        """Verify if the checkbox is checked."""
        element = self.element_base.element()
        result = self.element.is_selected()
        assert result == True, f"Expected checkbox to be checked, but it is not."
        return result
    
    def is_unchecked(self) -> bool:
        """Verify if the checkbox is unchecked."""
        element = self.element_base.element()
        result = element.is_selected()
        assert result == False, f"Expected checkbox to be unchecked, but it is not."
        return result

    