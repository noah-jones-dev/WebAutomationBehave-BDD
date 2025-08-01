from framework.fields.element_base import ElementBase
from framework.helpers.verifications.verify_static import VerifyStatic

class StaticField(ElementBase):
    
    @property
    def verify(self) -> VerifyStatic:
        """Returns a verifications object for this static field."""
        return VerifyStatic(self)
