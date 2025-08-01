from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from framework.helpers.waits import Waits
from selenium.webdriver.remote.webdriver import WebDriver

class WindowUtilities:
    
    @staticmethod
    def switch_to_new_window(driver: WebDriver):
        """Switches to the most recently opened window."""
        Waits.get_wait(driver).until(EC.new_window_is_opened(driver.window_handles))
        driver.switch_to.window(driver.window_handles[-1])
        
        
    @staticmethod
    def get_current_window(driver: WebDriver):
        return driver.current_window_handle

    @staticmethod
    def get_all_windows(driver: WebDriver):
        return driver.window_handles

    @staticmethod
    def switch_to_window(driver: WebDriver, window_id: str):
        driver.switch_to.window(window_id)
        
        