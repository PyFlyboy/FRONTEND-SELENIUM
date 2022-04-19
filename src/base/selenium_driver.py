from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import time
import os
import src.utilities.custom_logger as cl


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes a screenshot of the current page.
        """
        fileName = resultMessage + "." + str(round(time.time() *1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("###Exception occured when taking screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title



    def getByType(self, locatorType):

        locator_type = locatorType.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        else:
            self.log.info("Locator type "+ locator_type + " not correct/supported")
        return False


    def getElement(self,locator, locatorType='id', element=None):
        element = None
        try:
            locatorType = locatorType
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locatorType: "+ locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element


    def getElementlist(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        elements = []
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locatorType: " + locatorType)
        return elements


    def elementClick(self, locator, locatorType = 'id', element=None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Can'/t not click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()


    def sendKeys(self, data, locator, locatorType = 'id'):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: "+ locator + " locatorType: " + locatorType)
        except:
            self.log.info("Can'/t sent on the element with locator: " + locator + " locatorType: " + locatorType )


    def clearField(self, locator="", locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator + "locatorType: " + locatorType)


    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def isElementPresent(self, locator="", locatorType="id"):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
                if element is not None:
                    self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                    return True
                else:
                    self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                    return False
        except:
            print("Element not found")
            return False


    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                isDisplayed = True
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False


    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present.
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +" locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False


    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.2):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")


    def getElement2(self, locator, locatorType = 'id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element found')
        except:
            self.log.info('Element not found')
        return element


    def elementClick2(self, locator, locatorType = 'id'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element has been clicked with locator: " + locator + ' locatorType: ' + locatorType)
        except:
            self.log.info('Can not click on the element with locator: '+ locator + ' locatorType: ' + locatorType)


    def get_list_of_elements(self,locator, locatorType="id"):
        """
        Get list of elements
        """
        elements = []
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: ")
        except:
            self.log.info("Element list not found with locator: " + locator + " and locatorType: ")

        return elements



