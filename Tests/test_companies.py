import time

from Pages.BasePage import BasePage
from Pages.LivePage import LivePage


class Companies(BasePage):
    def test_Companies(self):
        lp = LivePage(self.driver)

        # tb.click_on_advertise_close()

        lp.click_on_companies()
        time.sleep(3)

