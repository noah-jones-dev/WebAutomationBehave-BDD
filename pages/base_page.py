from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from framework.helpers.scroll_directions import ScrollDirection
from framework.helpers.waits import Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._action = ActionChains(self.driver)
        
    @property
    def wait(self):
        return Waits.get_wait(self.driver)

    
    @property
    def action(self):
        return self._action
    
    
    def close_window(self):
        self.driver.close()
    
    
    def find_element(self, *locator: tuple):
        '''Finds a single element on the page using the provided locator. 
        Pass in a tuple with the locator strategy and value, e.g., (By.ID, 'element_id').'''
        return self.driver.find_element(*locator)
    
    
    def find_elements(self, *locator: tuple):
        '''Finds multiple elements on the page using the provided locator. 
        Pass in a tuple with the locator strategy and value, e.g., (By.CLASS_NAME, 'class_name').'''
        return self.driver.find_elements(*locator)
    
    def scroll(self, direction: ScrollDirection, amount: int = 1000):
        '''Scrolls the page by the given amount in the specified direction.'''
        if direction == ScrollDirection.UP:
            self.driver.execute_script(f"window.scrollBy(0, -{amount});")
        elif direction == ScrollDirection.DOWN:
            self.driver.execute_script(f"window.scrollBy(0, {amount});")
        elif direction == ScrollDirection.LEFT:
            self.driver.execute_script(f"window.scrollBy(-{amount}, 0);")
        elif direction == ScrollDirection.RIGHT:
            self.driver.execute_script(f"window.scrollBy({amount}, 0);")
            
    def ignore_adds(self):
        self.find_element(By.XPATH, "//div[@id='ltkpopup-close-button']").click()
            
    
    