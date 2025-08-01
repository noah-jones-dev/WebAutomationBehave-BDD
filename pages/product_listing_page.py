from pages.base_page import BasePage
from framework.fields.text_field import TextField
from selenium.webdriver.common.by import By
from framework.fields.list_field import ListField

class ProductListingPage(BasePage):
    
    @property
    def search_results_TB(self) -> TextField:
        """Returns the search results element."""
        return TextField(self.driver, [(By.XPATH, "//h1[contains(text(), 'Search Results')]")])
    
    @property
    def products_section_LS(self) -> ListField:
        """Returns the list of products displayed on the page."""
        return ListField(self.driver, [(By.XPATH, "//div[@data-sf-role='search-results']//ul//li")])