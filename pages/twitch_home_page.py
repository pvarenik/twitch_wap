import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TwitchHomePage(BasePage):
    URL = 'https://m.twitch.tv/'
    SEARCH_ICON = (By.CSS_SELECTOR, 'a[aria-label="Search"]')
    SEARCH_BAR = (By.CSS_SELECTOR, 'input[type="search"]')
    CLOSE_COOKIES_BUTTON = (By.CSS_SELECTOR, "[class^='ScCoreButtonLabel-']")
    ACCEPT_COOKIES_BUTTON = (By.LINK_TEXT, 'Accept')

    def load(self):
        self.driver.get(self.URL)

    def open_search(self):
        self.click(self.SEARCH_ICON)

    def search(self, query):
        self.type(self.SEARCH_BAR, query)
        self.press_enter(self.SEARCH_BAR)
        
    def close_cookies_click(self):
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE_COOKIES_BUTTON)
        )
        accept_button.click()
        
    def accept_cookies_click(self):
        BasePage.accept_cookies(self, self.ACCEPT_COOKIES_BUTTON)