import src.utilities.custom_logger as cl
import logging
from src.base.basepage import BasePage
from src.base.configuration import get_locator


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = get_locator()['LOGIN']


    def enterUserName(self, username=""):
        self.waitForElement(locator=self.locator['user_name'], locatorType='xpath')
        self.sendKeys(username, locator=self.locator['user_name'], locatorType='xpath')


    def enterPassword(self, password=""):
        self.sendKeys(password, locator=self.locator['password_field'], locatorType='css')


    def clickLoginButton(self):
        self.elementClick2(locator=self.locator['login_button'], locatorType='xpath')


    def clickErrorbutton(self):
        self.elementClick2(locator=self.locator['error_btn_confirmed'], locatorType="xpath")


    def clickUserSettings(self):
        self.elementClick2(locator=self.locator['user_settings_element'], locatorType="xpath")


    def login(self, username="", password=""):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        self.waitForElement(self.locator['user_settings_menu'], locatorType='xpath')
        result = self.isElementPresent(self.locator['user_settings_menu'], locatorType="xpath")
        return result


    def verifyLoginFailed(self):
        self.login(username="TestUser", password="2@#!")
        self.clickLoginButton()
        self.waitForElement(self.locator['login_failed_info'], locatorType="xpath")
        result = self.isElementDisplayed(self.locator['login_failed_info'],locatorType="xpath")
        return result


    def verifyLoggedUserName(self):
        self.waitForElement(self.locator['user_name_check'], locatorType="xpath")
        result = self.isElementPresent(self.locator['user_name_check'], lcatorType="xpath")
        return result


    def getUserName(self):
        self.screenShot("LogginSuccesful")
        result = self.getText(self.locator['user_name_check'], locatorType="xpath")
        return result


    def logout(self):
        self.waitForElement(self.locator['user_settings_menu'],locatorType="xpath")
        self.elementClick2(locator=self.locator['user_settings_menu'], locatorType='xpath')
        self.waitForElement(self.locator['logout_btn'],locatorType="xpath")
        # self.elementClick(element=logoutLinkElement)
        self.elementClick2(self.locator['logout_btn'],
                           locatorType="xpath")


    def login_window_title(self):
        self.waitForElement(locator=self.locator['login_title'], locatorType='xpath')
        self.isElementPresent(locator=self.locator['login_title'], locatorType='xpath')

