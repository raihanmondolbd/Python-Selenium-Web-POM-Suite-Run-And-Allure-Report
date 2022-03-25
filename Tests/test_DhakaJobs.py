import time

from Pages.BasePage import BasePage
from Pages.DivisionalPage import DivisionalPage


class Companies(BasePage):
    def test_Companies(self):
        lp = DivisionalPage(self.driver)

        # tb.click_on_advertise_close()

        lp.click_on_dhaka_jobs()
        time.sleep(3)

