from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.fields.text_field import TextField
from framework.fields.list_field import ListField
from framework.fields.link_field import LinkField
from framework.fields.checkbox_field import CheckboxField
from framework.fields.button_field import ButtonField
from framework.fields.static_field import StaticField
from framework.fields.nav_field import NavField

class HomePage(BasePage):
    
    @property 
    def main_header_tag_ST(self) -> StaticField:
        """Returns the main header tag static field."""
        return StaticField(self.driver, [(By.XPATH, "//p[@class='hero-tag']")])

    @property
    def main_header_ST(self) -> StaticField:
        """Returns the main header static field."""
        return StaticField(self.driver, [(By.XPATH, "//h1[@class='hero-header']")])
    
    @property
    def main_header_description_ST(self) -> StaticField:
        """Returns the main header description static field."""
        return StaticField(self.driver, [(By.XPATH, "//div[@class='hero-description']/p")])
    
    @property
    def search_TB(self) -> TextField:
        """Returns the search text field."""
        field = TextField(self.driver, [(By.XPATH, "//a[@id='search']"), (By.XPATH, "//input[@id='search-input']")])
        field.reveal()
        return field
        
    @property
    def language_selector_LS(self) -> ListField:
        """Returns the language selector dropdown list."""
        field = ListField(self.driver, [(By.ID, "language"), (By.XPATH, "//div[@class='dropdown-menu language show']//ul//a")])
        field.reveal()
        return field
    
    @property
    def menu_NV(self) -> NavField:
        """Returns the menu navigation field."""
        return NavField(self.driver, [(By.ID, "mobile-nav-toggle")], False)

    @property
    def free_coloring_pages_LK(self) -> LinkField:
        """Returns the 'Free Coloring Pages' link."""
        return LinkField(self.driver, "Free Coloring Pages")
    
    @property
    def adult_coloring_pages_LK(self) -> LinkField:
        """Returns the 'Adult Coloring Pages' link."""
        return LinkField(self.driver, "Adult Coloring Pages")
    
    @property
    def plants_and_animals_free_coloring_pages_LK(self) -> LinkField:
        """Returns the 'Plants And Animals Free Coloring Pages' link."""
        return LinkField(self.driver, "Plants And Animals Free Coloring Pages")
    
    @property
    def email_address_TB(self) -> TextField:
        """Returns the email address input field."""
        return TextField(self.driver, [(By.XPATH, "//input[@id='FooterEmail']")])
    
    @property
    def i_agree_to_terms_and_conditions_CB(self) -> CheckboxField:
        """Returns the 'I Agree To Terms And Conditions' checkbox."""
        return CheckboxField(self.driver, [(By.XPATH, "//input[contains(@aria-label, 'I agree to the Crayola')]")])
    
    @property
    def about_us_support_LS(self) -> ListField:
        """Returns the 'About Us' list of links."""
        return ListField(self.driver, [(By.XPATH, "//nav[@aria-label='Footer Support Links']/ul/li")])
        
    @property
    def email_address_submit_BTN(self) -> ButtonField:
        """Returns the 'Submit' button for the email address field."""
        return ButtonField(self.driver, [(By.XPATH, "//div[@class='footer-input-wrap']/div[@data-sf-role='submit-button-container']/button")])

    def open(self):
        """Open the Crayola home page."""
        self.driver.get("https://www.crayola.com/")