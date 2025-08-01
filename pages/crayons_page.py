from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from framework.fields.static_field import StaticField
from framework.fields.text_field import TextField
from framework.fields.list_field import ListField

class CrayonsPages(BasePage):
    
    @property
    def page_title(self) -> StaticField:
        """Returns the page title static field."""
        return StaticField(self.driver, [(By.XPATH, "//div[@class='hero-inner']/h1")])
    
    @property
    def page_description(self) -> StaticField:
        """Returns the page description static field."""
        return StaticField(self.driver, [(By.XPATH, "//div[@class='hero-description']//p")])
    
    
    @property
    def search_results_TB(self) -> TextField:
        """Returns the search results element."""
        return TextField(self.driver, [(By.XPATH, "//p[contains(@class, 'item-list-results')]")])
    
    @property
    def products_section_LS(self) -> ListField:
        """Returns the list of products displayed on the page."""
        return ListField(self.driver, [(By.XPATH, "//div[@id='list-section']/ul/li")])