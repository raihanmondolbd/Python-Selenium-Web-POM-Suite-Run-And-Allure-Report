import time

from Pages.BasePage import BasePage
from Pages.LivePage import LivePage


class Vacancies(BasePage):
    def test_Vacancies(self):
        lp = LivePage(self.driver)

        # tb.click_on_advertise_close()

        lp.click_on_vacancies()
        time.sleep(3)

