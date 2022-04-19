from src.pages.login_page import LoginPage
import unittest
import pytest
import src.utilities.custom_logger as tl
import logging
import time
from src.utilities.teststatus import TestStatus
from src.base.configuration import get_credentials

@pytest.mark.usefxtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = tl.customLogger(logging.DEBUG)

    @pytest.fixture()
    def objectSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.creden = get_credentials()['USER']

    @pytest.mark.usefixtures("objectSetup")
    @pytest.mark.tcid1
    def test_t1_valid_login(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1validLogin")
        self.log.info("*#" * 20)
        self.lp.login(username=self.creden['user_name'], password=self.creden['psswd'])
        login_result = self.lp.verifyLoginSuccessful()
        assert login_result == True, self.log.error("ASSERTION FAILED!")
        self.ts.mark(login_result,"User is logged in")
        self.lp.logout()
        logout_result = self.lp.login_window_title()
        assert logout_result == True
        self.ts.markFinal("test_t1validLogin", result=logout_result, resultMessage="TEST: User logged in and logged out.")

    @pytest.mark.usefixtures("objectSetup")
    @pytest.mark.tcid2
    def test_t2_invalid_login(self):
        self.log.info("*#" * 20)
        self.log.info("test_t2invalidLogin")
        self.log.info("*#" * 20)
        time.sleep(3)
        result = self.lp.verifyLoginFailed()
        assert result == True, self.log.error("ASSERTION FAILED!")
        self.lp.clickErrorbutton()
        self.ts.markFinal("test_t2invalidLogin", result=result, resultMessage="TEST: Input invalid user credentials.")






