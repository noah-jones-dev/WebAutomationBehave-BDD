from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep, time

class Waits: 
    
    @staticmethod
    def get_wait(driver: WebDriver, timeout: int = 10):
        if not hasattr(driver, "_wait"):
            driver._wait = WebDriverWait(driver, timeout)
        return driver._wait
    
    
    # @staticmethod
    # def wait_for_ads(driver: WebDriver, timeout: int = 10):
    #     """Waits for ads to be present and attempts to close them (handles multiple)."""
    #     xpath = "//div[@id='ltkpopup-close-button'] | //div[@aria-modal='true']//div[contains(@id, 'close-btn')]"
    #     closed_any = False
    #     for _ in range(timeout):
    #         try:
    #             ads = driver.find_elements(By.XPATH, xpath)
    #             if ads:
    #                 for ad in ads:
    #                     if ad.is_displayed():
    #                         try:
    #                             ad.click()
    #                             closed_any = True
    #                             print("Ad closed successfully.")
    #                         except Exception as e:
    #                             print(f"Ad found but not clickable: {e}")
    #         except NoSuchElementException:
    #             pass
    #         sleep(1)
    #     if not closed_any:
    #         print("Ads not found or timed out.")


    @staticmethod
    def wait_for_ads(driver: WebDriver, timeout: int = 10):
        """Waits for ads to be present and attempts to close them.
        Exits early if at least two ad types are found and closed."""
        locators = [
            "//div[@aria-modal='true']//div[contains(@id, 'close-btn')]",
            "//div[@id='ltkpopup-content']//button[@class='ltkpopup-close']"
        ]
        closed_any = False
        start_time = time()
        while time() - start_time < timeout:
            found_this_round = set()  # track which ad types were found and closed
            for xpath in locators:
                try:
                    ads = driver.find_elements(By.XPATH, xpath)
                    for ad in ads:
                        if ad.is_displayed():
                            try:
                                ad.click()
                                closed_any = True
                                found_this_round.add(xpath)
                                print(f"Ad closed successfully using locator: {xpath}")
                            except (ElementClickInterceptedException, Exception) as e:
                                print(f"Ad found but not clickable with locator {xpath}: {e}")
                except NoSuchElementException:
                    continue
            # Exit early if at least 2 different ad types were found and closed
            if len(found_this_round) >= 2:
                print("At least two ad types found and closed. Exiting early.")
                return
            sleep(1)
        if not closed_any:
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
