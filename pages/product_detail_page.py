from pages.base_page import BasePage
from framework.fields.button_field import ButtonField
from framework.fields.static_field import StaticField
from framework.fields.list_field import ListField
from selenium.webdriver.common.by import By
from framework.helpers.waits import Waits
class ProductDetailPage(BasePage):
    
    @property
    def product_title_ST(self) -> StaticField:
        """Returns the product title element."""
        return StaticField(self.driver, [(By.XPATH, "//div[contains(@class, 'content-detail')]/h1")])
    
    @property
    def where_to_buy_BTN(self) -> ButtonField:
        """Returns the 'Where to Buy' button element."""
        return ButtonField(self.driver, [(By.XPATH, "//div[@role='button'][span[text()='Where to Buy']]")])
    
    @property 
    def modal_product_title_ST(self) -> StaticField:
        """Returns the product title in the modal."""
        Waits.wait_for_modal(self.driver)
        return StaticField(self.driver, [(By.XPATH, "//div[@class='ps-product-details']/h2")])
    
    @property
    def modal_product_availability_LS(self) -> ListField:
        """Returns the list of product availability elements in the modal."""
        Waits.wait_for_modal(self.driver)
        return ListField(self.driver, [(By.XPATH, "//ul[@class='ps-online-sellers']/li")])