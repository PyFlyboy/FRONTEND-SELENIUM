import logging
from src.base.selenium_driver import SeleniumDriver
from traceback import print_stack
from src.utilities.util import Util
import src.utilities.custom_logger as cl
from src.base.configuration import get_locator as locator
"""

Base Page class implementation
It implements methods which are common to all the pages throughout the application

"""

class BasePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()
        self.locator = locator()['BASEPAGE']

    def login(self, username="", password=""):
        self.waitForElement(locator=self.locator['user_name'], locatorType='xpath')
        self.sendKeys(username, locator=self.locator['user_name'], locatorType='xpath')
        self.sendKeys(password, locator=self.locator['password_field'], locatorType='css')
        self.elementClick2(locator=self.locator['login_button'], locatorType='xpath')


    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def navigate_to_my_profile(self):
        self.elementClick(locator=self.locator['my_profile'])

    def navigate_to_workflow(self):
        self.elementClick(locator=self.locator['workflow'])

    def navigate_to_workflow_task(self):
        self.elementClick(locator=self.locator['workflowtask'])

    def navigate_to_calendar(self):
        self.elementClick(locator=self.locator['calendar'])

    def navigate_to_announcements(self):
        self.waitForElement(locator=self.locator['announcements'])
        self.elementClick(locator=self.locator['announcements'])

    def navigate_to_subordinate(self):
        self.elementClick(locator=self.locator['subordinate'])

    def navigate_to_holidays(self):
        self.elementClick(locator=self.locator['holiday'])

    def navigate_to_loan(self):
        self.elementClick(locator=self.locator['loan'])

    def navigate_to_knowlage(self):
        self.elementClick(locator=self.locator['knowlage'])

    def navigate_to_langexam(self):
        self.elementClick(locator=self.locator['langexam'])
