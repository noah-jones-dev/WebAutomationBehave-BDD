from framework.helpers.verifications.verify_base import VerifyBase

class VerifyStatic(VerifyBase):
    
    def text_contains(self, text: str):
        '''Verify that the element contains the expected text.'''
        element = self.element_base.element()
        assert text in element.text, f"Expected text '{text}' not found in element text '{element.text}'."
        
        
    def text_is(self, text: str):
        '''Verify that the element is the expected text.'''
        element = self.element_base.element()
        assert text == element.text, f"Expected text '{text}' not found in element text '{element.text}'."
        
        
    