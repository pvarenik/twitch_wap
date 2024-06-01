
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_twitch_search(driver):
    home_page = TwitchHomePage(driver)
    search_results_page = TwitchSearchResultsPage(driver)
    streamer_page = TwitchStreamerPage(driver)

    home_page.load()
    home_page.close_cookies_click()
    home_page.open_search()
    home_page.search("StarCraft II")

    # Scroll down twice
    for _ in range(2):
        home_page.scroll_down()

    search_results_page.select_streamer()
    streamer_page.wait_for_stream_to_load()
    streamer_page.take_screenshot('streamer_page_mobile.png')