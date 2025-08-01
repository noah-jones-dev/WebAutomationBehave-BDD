from operator import index
from framework.fields.element_base import ElementBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class NavField(ElementBase):
    
    def __init__(self, driver: WebDriver, locators: list[tuple[By, str]], menu: bool):
        super().__init__(driver, locators)
        self.menu = menu
        if (menu):
            self.element().click()
            self.locator_format = ""
        else:
            self.locator_format = "//a[contains(text(), '{0}')]"
            self.locator_header_format = "//a/span[contains(text(), '{0}')]"

    def navigate_to(self, path: list[str]):
        """Navigate to a specific page by clicking the links in the path."""
        for index, item in enumerate(path): 
            if index == 0 and not self.menu:
                try:
                    element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.locator_header_format.format(item))))
                except Exception as exception:
                    print(f"Failed to find element for {item}: {exception}")
                    continue
                element.click()
            else:
                try:
                    element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.locator_format.format(item))))
                except Exception as exception:
                    print(f"Failed to find element for {item}: {exception}")
                    continue
                element.click()
        return self
    