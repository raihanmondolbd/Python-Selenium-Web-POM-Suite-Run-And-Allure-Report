import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage

class LoginTest(BasePage):
    def test_login_page(self):

        loginPage = LoginPage(self.driver)
        # loginPage.click_on_advertise_close()
        loginPage.click_on_login()
        time.sleep(3)
        loginPage.click_on_login2()
        time.sleep(3)
        loginPage.enter_email("Your Email")
        time.sleep(3)
        loginPage.click_next()
        time.sleep(3)
        loginPage.enter_password("Your Password")
        time.sleep(3)
        loginPage.click_login3()
