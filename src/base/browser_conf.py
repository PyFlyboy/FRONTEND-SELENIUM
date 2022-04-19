import traceback
from selenium import webdriver
import os
from selenium.webdriver.chrome import options
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from decouple import config

class BrowserConfiguration():

    def __init__(self, browser):
        self.browser = browser

    # def WebDriverInstance(self):
    #     """
    #     Get WebDriver instance based on the browser configuration
    #     """
    #     if self.browser == "chrome":
    #         desiredCapabilities = DesiredCapabilities.CHROME
    #     elif self.browser == "firefox":
    #         desiredCapabilities = DesiredCapabilities.FIREFOX
    #     elif self.browser == "edge":
    #         desiredCapabilities = DesiredCapabilities.EDGE
    #     else:
    #         desiredCapabilities = DesiredCapabilities.CHROME
    #     desiredCapabilities['acceptInsecureCerts'] = True
    #     desiredCapabilities['acceptSslCerts'] = True
    #     driver = webdriver.Remote(command_executor=config('SWARM_HUB_SELENIUM'),
    #                               desired_capabilities=desiredCapabilities)
    #     baseURL = config('APP_URL')
    #     driver.get(baseURL)
    #     return driver

    def WebDriverInstance(self):

        baseURL = config('APP_URL')
        #driver_options = Options()
        # driver_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        if self.browser == 'chrome':
            #driver = webdriver.Chrome(options=driver_options)
            driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()
            # driver = webdriver.Chrome(options=driver_options)

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver


