from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep



class Waits: 
    
    @staticmethod
    def get_wait(driver: WebDriver, timeout: int = 10):
        if not hasattr(driver, "_wait"):
            driver._wait = WebDriverWait(driver, timeout)
        return driver._wait
    
    
    @staticmethod
    def wait_for_ads(driver: WebDriver, timeout: int = 10):
        '''Waits for ads to be present and attempts to close them.'''
        for count in range(timeout):
            try:
                ad = driver.find_element(By.XPATH, "//div[@id='ltkpopup-close-button']")
                modal = driver.find_element(By.XPATH, "//div[@aria-modal='true']//div[contains(@id, 'close-btn')]")
                if ad.is_displayed():
                    ad.click()
                    print("Ads closed successfully.")
                if modal.is_displayed():
                    modal.click()
                    print("Modal closed successfully.")    
                return
            except NoSuchElementException:
                pass
            sleep(1)
        print("Ads not found or timed out.")
        
    @staticmethod
    def wait_for_modal(driver: WebDriver, timeout: int = 5):
        """Waits for a modal to be present and returns it."""
        for count in range(timeout):
            try:
                modal = driver.find_element(By.XPATH, "//div[@class='ps-header']")
                if modal.is_displayed():
                    print("Modal is displayed.")
                    return modal
            except NoSuchElementException:
                print("Modal not found, retrying...")
            sleep(1)
        raise TimeoutException("Modal did not appear within the specified timeout.")
