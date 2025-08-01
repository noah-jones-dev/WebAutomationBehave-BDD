
class VerifyBase():
    
    def __init__(self, element: 'ElementBase'):
        self.element_base = element
        
    def exists(self):
        '''Verify that the element exists.'''
        element = self.element_base.element()
        assert element is not None, "Element does not exist."
        
    def not_exists(self):
        '''Verify that the element does not exist.'''
        element = self.element_base.element()
        assert element is None, "Element does exist."