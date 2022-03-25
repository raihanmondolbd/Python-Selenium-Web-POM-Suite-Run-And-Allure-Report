import time

from Pages.BasePage import BasePage
from Pages.LivePage import LivePage


class NewJobs(BasePage):
    def test_NewJobs(self):
        lp = LivePage(self.driver)

        # tb.click_on_advertise_close()

        lp.click_on_new_jobs()
        time.sleep(3)

