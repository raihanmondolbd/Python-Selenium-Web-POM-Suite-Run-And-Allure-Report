import time

from Pages.BasePage import BasePage
from Pages.LivePage import LivePage


class LiveJobs(BasePage):
    def test_LiveJobs(self):
        lp = LivePage(self.driver)

        # tb.click_on_advertise_close()

        lp.click_on_live_jobs()
        time.sleep(3)

