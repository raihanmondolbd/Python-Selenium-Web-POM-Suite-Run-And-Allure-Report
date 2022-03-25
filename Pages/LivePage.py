from Pages.HomePage import HomePage
from Locators.Locators import LivePageLocators


class LivePage(HomePage):

    def __init__(self, driver):
        self.locator = LivePageLocators
        self.driver = driver
        super(LivePage, self).__init__(driver)

    def click_on_live_jobs(self):
        self.find_element(*self.locator.livejobs).click()

    def click_on_vacancies(self):
        self.find_element(*self.locator.vacancies).click()

    def click_on_companies(self):
        self.find_element(*self.locator.companies).click()

    def click_on_new_jobs(self):
        self.find_element(*self.locator.newjobs).click()





