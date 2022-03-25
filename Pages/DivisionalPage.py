from Pages.HomePage import HomePage
from Locators.Locators import DivisionalPageLocators


class DivisionalPage(HomePage):

    def __init__(self, driver):
        self.locator = DivisionalPageLocators
        self.driver = driver
        super(DivisionalPage, self).__init__(driver)

    def click_on_dhaka_jobs(self):
        self.find_element(*self.locator.dhakajobs).click()

    def click_on_barishal_jobs(self):
        self.find_element(*self.locator.barishal).click()

    def click_on_khulna_jobs(self):
        self.find_element(*self.locator.khulna).click()

    def click_on_sylhet_jobs(self):
        self.find_element(*self.locator.sylhet).click()





