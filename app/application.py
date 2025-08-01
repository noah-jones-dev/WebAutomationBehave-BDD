from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage
from pages.product_detail_page import ProductDetailPage
from pages.crayons_page import CrayonsPages

class Application():
    
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.home_page = HomePage(driver)
        self.product_listing_page = ProductListingPage(driver)
        self.product_detail_page = ProductDetailPage(driver)
        self.crayons_page = CrayonsPages(driver)
