from Pages.HomePage import HomePage
from Locators.Locators import JobSearch


class JobSearchPage(HomePage):

    def __init__(self, driver):
        self.locator = JobSearch
        self.driver = driver
        super(JobSearchPage, self).__init__(driver)

    def click_on_advertise_close(self):
        self.find_element(*self.locator.advertise_xpath).click()

    def enter_job_type_text(self):
        self.find_element(*self.locator.jobsearch_textbox_xpath).send_keys("QA Engineer")

    def click_organization_type(self):
        self.find_element(*self.locator.organization_type_xpath).click()

    def select_organization_type_government(self):
        self.find_element(*self.locator.government_jobs_xpath).click()

    def select_organization_type_semi_government(self):
        self.find_element(*self.locator.semi_government_jobs_xpath).click()

    def select_organization_type_ngo(self):
        self.find_element(*self.locator.ngo_jobs_xpath).click()

    def select_organization_type_private_firm(self):
        self.find_element(*self.locator.private_firm_xpath).click()

    def select_organization_type_international_agencies(self):
        self.find_element(*self.locator.international_agencies_xpath).click()

    def select_organization_type_others(self):
        self.find_element(*self.locator.others_jobs_xpath).click()

    def click_search(self):
        self.find_element(*self.locator.job_search_button_xpath).click()
