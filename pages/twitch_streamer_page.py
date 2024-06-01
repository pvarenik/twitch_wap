from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TwitchStreamerPage(BasePage):
    STREAM_PLAYER = (By.CSS_SELECTOR, 'video')

    def wait_for_stream_to_load(self):
        self.wait_for_element(self.STREAM_PLAYER)

    def take_screenshot(self, filename):
        super().take_screenshot(filename)