from framework.fields.element_base import ElementBase
from framework.helpers.verifications.verify_link import VerifyLink
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LinkField(ElementBase):
    
    LINK_LOCATOR_FORMAT = "//a[@class='be-related-link'][text()='{0}']"
    
    def __init__(self, driver: WebDriver, name: str):
        locator = (By.XPATH, self.LINK_LOCATOR_FORMAT[1].format(name))
        super().__init__(driver, [locator])
    
    @property
    def verify(self) -> VerifyLink:
        """Returns a verifications object for this link field."""
        return VerifyLink(self)