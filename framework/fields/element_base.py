from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from framework.helpers.waits import Waits
from selenium.webdriver.remote.webdriver import WebDriver


class ElementBase():
    
    def __init__(self, driver: WebDriver, locators: list[tuple[By, str]]):
        self.driver = driver
        self.alert = Alert(self.driver)
        self.action = ActionChains(self.driver)
        self.locators = locators 

    @property
    def wait(self):
        return Waits.get_wait(self.driver)
        
    def element(self):
        final_locator = self.locators[-1]
        return self.wait.until(EC.presence_of_element_located(final_locator))
    
    def elements(self):
        final_locator = self.locators[-1]
        return self.wait.until(EC.presence_of_all_elements_located(final_locator))
    
    def click(self):
        return self.element().click()
    
    def reveal(self):
        '''Reveals the element by clicking through all locators if multiple are provided. Returns the last element.'''
        if len(self.locators) > 1:
            for locator in self.locators[:-1]:
                try:
                    self.wait.until(EC.element_to_be_clickable(locator)).click()
                except Exception as exception:
                    print(f"Failed to click {locator}: {exception}") 
        return self.wait.until(EC.element_to_be_clickable(self.locators[-1]))
    
    def scroll_to(self, element=None):
        if element is None:
            element = self.element()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.execute_script(
            "var elem = arguments[0];"
            "var rect = elem.getBoundingClientRect();"
            "return (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight));",
            element
        ))
        return self
    