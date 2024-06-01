from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def type(self, locator, text):
        self.find_element(locator).send_keys(text)

    def press_enter(self, locator):
        self.find_element(locator).send_keys(Keys.RETURN)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def take_screenshot(self, filename):
        self.driver.save_screenshot('screenshots/' + filename)

    def accept_cookies(self, locator):
        try:
            self.click(self, locator)
        except Exception as e:
            print(f"No cookies button found: {e}")