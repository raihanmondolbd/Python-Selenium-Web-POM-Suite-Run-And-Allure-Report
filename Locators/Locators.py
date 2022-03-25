from selenium.webdriver.common.by import By

class LogIn():
    advertise_xpath = (By.XPATH, '//div/a/img[@alt="Close Main popup"]')
    signIn_xpath = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a')
    signIn_xpath2 = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li/div[1]/div[2]/div[3]/a[1]')
    email_textbox_xpath = (By.XPATH, '//*[@id="TXTUSERNAME"]')
    next_button_xpath = (By.XPATH, '//div/input[@value="Next"]')
    password_button_xpath = (By.XPATH, '//*[@id="TXTPASS"]')
    signIn_xpath3 = (By.XPATH, '//div/input[@value="Sign in"]')
    facebook_button_xpath = (By.XPATH,'//*[@id="fb_button"]')

class TopBar():
    advertise_xpath = (By.XPATH, '//div/a/img[@alt="Close Main popup"]')
    mybdjobs_xpath = (By.XPATH, '//*[@id="lin_header_top02"]/div/div/div/div/ul/li[2]/a')
    elearning_xpath = (By.XPATH, '//*[@id="lin_header_top02"]/div/div/div/div/ul/li[3]/a')
    tender_xpath = (By.XPATH, '//*[@id="lin_header_top02"]/div/div/div/div/ul/li[4]/a')
    employers_xpath = (By.XPATH, '//*[@id="lin_header_top02"]/div/div/div/div/ul/li[5]/a')

class JobSearch():
    advertise_xpath = (By.XPATH, '//div/a/img[@alt="Close Main popup"]')
    jobsearch_textbox_xpath = (By.XPATH, '//*[@id="txtKeyword"]')
    organization_type_xpath = (By.XPATH, '//*[@id="qOT"]')
    job_search_button_xpath = (By.XPATH, '//*[@id="main"]/div/div[1]/div/div[1]/form/input[2]')
    government_jobs_xpath = (By.XPATH, '//*[@id="qOT"]/option[@value="1"]')
    semi_government_jobs_xpath = (By.XPATH, '//*[@id="qOT"]/option[@value="2"]')
    ngo_jobs_xpath = (By.XPATH, '//*[@id="qOT"]/option[@value="3"]')
    private_firm_xpath = (By.XPATH, '//*[@id="qOT"]/option[@value="4"]')
    international_agencies_xpath = (By.XPATH, '//*[@id="qOT"]/option[@value="5"]')
    others_jobs_xpath = (By.XPATH, '//*[@id="qOT"]/option[@value="6"]')

class LivePageLocators():
    livejobs = (By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/a[1]/div/div')
    vacancies = (By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/a[2]/div/div')
    companies = (By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/a[3]/div/div')
    newjobs = (By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/a[4]/div/div')

class DivisionalPageLocators():
    dhakajobs = (By.XPATH, '//*[@id="main"]/div/div[2]/div/div[1]/div/a[1]')
    barishal = (By.XPATH, '//*[@id="main"]/div/div[2]/div/div[1]/div/a[2]')
    khulna = (By.XPATH, '//*[@id="main"]/div/div[2]/div/div[1]/div/a[3]')
    sylhet = (By.XPATH, '//*[@id="main"]/div/div[2]/div/div[1]/div/a[4]')

