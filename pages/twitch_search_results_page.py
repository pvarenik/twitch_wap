from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TwitchSearchResultsPage(BasePage):
    STREAMER_LINK = (By.CSS_SELECTOR, 'img[class="tw-image"]')

    def select_streamer(self):
        self.wait_for_element(self.STREAMER_LINK)
        self.click(self.STREAMER_LINK)