import time
import src.utilities.custom_logger as cl
import logging
from src.base.basepage import BasePage

import time as tm
from src.base.configuration import get_credentials, get_locator



class AnnouncementsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login(username=get_credentials()['USER']['user_name'], password=get_credentials()['USER']['psswd'])
        self.navigate_to_announcements()
        self.locator = get_locator()['ANNOUNCEMENTS']

    def clear_field(self):
        searchField = self.getElement(locator=self.locator['search_window'], locatorType='css')
        searchField.clear()


    def search_for_element(self, element):
        self.elementClick2(locator=self.locator['search_window'], locatorType='css')
        self.sendKeys(element, locator=self.locator['search_window'], locatorType='css')
        self.elementClick2(self.locator['search_btn'])


    def verify_archive_action(self):
        self.waitForElement(locator=self.locator['archive_action'], locatorType='xpath')
        result = self.isElementPresent(locator=self.locator['archive_action'], locatorType='xpath')
        return result


    def verify_mark_as_read_action(self):
        self.waitForElement(locator=self.locator['archive_action'], locatorType='xpath')
        result = self.isElementPresent(locator=self.locator['archive_action'], locatorType='xpath')
        return result


    def get_unread_msg_id(self):
        self.waitForElement(locator=self.locator['unread_msg'], locatorType="xpath")
        unread_msg = self.get_list_of_elements(locator=self.locator['unread_msg'], locatorType="xpath")
        if len(unread_msg) != 0:
            unread_msg_id= unread_msg[0].get_attribute("id")
            return unread_msg_id
        return None

    def get_read_msg_id(self):
        self.waitForElement(locator=self.locator['read_msg'], locatorType="xpath")
        readed_msg = self.get_list_of_elements(locator=self.locator['read_msg'], locatorType="xpath")
        if len(readed_msg) != 0:
            msg_id = readed_msg[0].get_attribute("id")
            return msg_id
        return None


    def get_archived_msg_id(self):
        self.waitForElement(locator=self.locator['archived_msg'], locatorType="xpath")
        archived_msg = self.get_list_of_elements(locator=self.locator['archived_msg'], locatorType="xpath")
        if len(archived_msg) != 0:
            msg_id= archived_msg[0].get_attribute("id")
            return msg_id
        return None


    def get_unread_msg_title(self, msg_id=None):
        msg_id = self.get_unread_msg_id()
        if msg_id != None:
            msg_id = str(msg_id)
            id_number = msg_id.lstrip('msg')
            title_msg_locator = "//div[@id='msg"+ id_number +"']//div[@class='name']"
            element_locator = title_msg_locator
            title_name = self.getText(locator=element_locator, locatorType='xpath')
            return {title_msg_locator:title_name}
        else:
            return None


    def get_read_msg_title(self, msg_id=None):
        msg_id = self.get_read_msg_id()
        if msg_id != None:
            msg_id = str(msg_id)
            id_number = msg_id.lstrip('msg')
            title_msg_locator = "//div[@id='msg"+id_number+"']//div[@class='name']"
            element_locator = title_msg_locator
            title_name = self.getText(locator=element_locator, locatorType='xpath')
            return {title_msg_locator:title_name}
        else:
            return None


    def get_archived_msg_title(self, msg_id=None):
        msg_id = self.get_archived_msg_id()
        if msg_id != None:
            id_number = msg_id.lstrip('msg')
            title_msg_locator = "//div[@id='msg"+id_number+"']//div[@class='name']"
            element_locator = title_msg_locator
            title_name = self.getText(locator=element_locator, locatorType='xpath')
            return {title_msg_locator:title_name}
        else:
            return None


    def get_content_of_unread_msg(self):
        msg_id = self.get_unread_msg_id()
        if msg_id != None:
            id_number = msg_id.lstrip('msg')
            element_locator = self.locator['content_msg']
            content = self.getText(locator=element_locator, locatorType='xpath')
            return content
        return None


    def get_content_of_read_msg(self):
        msg_id = self.get_read_msg_id()
        if msg_id != None:
            id_number = msg_id.lstrip('msg')
            element_locator = self.locator['content_msg']
            content = self.getText(locator=element_locator, locatorType='xpath')
            return content
        return None

    def serach_for_element_check(self, msg_not_archived=False, msg_archived = False, msg_all = False):

        if msg_not_archived == True:
            self.clearField(locator=self.locator['search_window'], locatorType='css')
            element = self.get_unread_msg_title()
            if element != None:
                for key in element.keys():
                    element_locator = key
                for val in element.values():
                    element_searched = val
                serach_window = self.sendKeys(data=element_searched, locator=self.locator['search_window'], locatorType='css')
                self.elementClick(locator=self.locator['search_btn'], locatorType='id')
                result = self.isElementDisplayed(locator=element_locator, locatorType='xpath')
                self.elementClick(locator=self.locator['msg_btn_clear'], locatorType='id')
                if result == True:
                    return True
                else:
                    result = False
                    return False
            else:
                element = self.get_read_msg_title()
                if element != None:
                    for key in element.keys():
                        element_locator = key
                    for val in element.values():
                        element_searched = val
                    serach_window = self.sendKeys(data=element_searched, locator=self.locator['search_window'], locatorType='css')
                    self.elementClick(locator=self.locaator['search_btn'], locatorType='id')
                    result = self.isElementDisplayed(locator=element_locator, locatorType='xpath')
                    self.elementClick(locator=self.locator['msg_btn_clear'], locatorType='id')
                    if result == True:
                        return True
                    else:
                        return False
                self.log.error("TUTAJ JAKIS SENSOWNY KOMENTARZ DO LOGOW")
                return None

        elif msg_archived == True:
            self.elementClick(locator=self.locator['radio_archived'])
            self.clearField(locator=self.locator['search_window'], locatorType='css')
            self.waitForElement(locator=self.locator['msg_list'], locatorType="xpath")
            element = self.get_archived_msg_title()
            if element != None:
                for key in element.keys():
                    element_locator = key
                for val in element.values():
                    element_searched = val
                serach_window = self.sendKeys(data=element_searched, locator=self.locator['search_window'], locatorType='css')
                self.elementClick(locator=self.locator['search_btn'], locatorType='id')
                result = self.isElementDisplayed(locator=element_locator, locatorType='xpath')
                self.elementClick(locator=self.locator['msg_btn_clear'], locatorType='id')
                if result == True:
                    return True
                else:
                    return False
            else:
                self.log.error("TUTAJ JAKIS SENSOWNY KOMENTARZ DO LOGOW")
                return None

        elif msg_all == True:
            self.elementClick(locator=self.locator['radio_all'], locatorType='id')
            self.waitForElement(locator=self.locator['msg_list'], locatorType="xpath")
            element = self.get_read_msg_title()
            if element != None:
               for key in element.keys():
                    element_locator = key
               for val in element.values():
                    element_searched = val
               serach_window = self.sendKeys(data=element_searched, locator=self.locator['search_window'], locatorType='css')
               self.elementClick(locator=self.locator['search_btn'], locatorType='id')
               result = self.isElementDisplayed(locator=element_locator, locatorType='xpath')
               self.elementClick(locator=self.locator['msg_btn_clear'], locatorType='id')
               if result == True:
                    return True
               else:
                    return False
            else:
                element = self.get_unread_msg_title()
                if element != None:
                    for key in element.keys():
                        element_locator = key
                    for val in element.values():
                        element_searched = val
                    serach_window = self.sendKeys(data=element_searched, locator=self.locator['search_window'], locatorType='css')
                    self.elementClick(locator=self.locator['search_btn'], locatorType='id')
                    result = self.isElementDisplayed(locator=element_locator, locatorType='xpath')
                    if result == True:
                        return True
                    else:
                        return False
                self.log.error("TUTAJ JAKIS SENSOWNY KOMENTARZ DO LOGOW")
                return None

            self.log.error("TUTAJ JAKIS SENSOWNY KOMENTARZ DO LOGOW")
            return None

    def page_elements(self):

        result = []
        title_page = self.isElementDisplayed(locator=self.locator['header_title'], locatorType='xpath', element='Ogłoszenia')
        search_btn = self.isElementDisplayed(locator=self.locator['search_window'], locatorType='css')
        radio_all = self.isElementDisplayed(locator=self.locator['radio_all'], locatorType='id')
        radio_archived = self.isElementDisplayed(locator=self.locator['radio_archived'], locatorType='id')
        radio_not_archived = self.isElementDisplayed(locator=self.locator['radio_not_archived'], locatorType='id')
        menu = self.isElementDisplayed(locator=self.locator['radio_not_archived'], locatorType='id')
        user_menu = self.isElementDisplayed(locator=self.locator['menu'], locatorType='xpath')
        user_icon = self.isElementDisplayed(locator=self.locator['user_icon'], locatorType='xpath')
        result.extend([title_page,search_btn,radio_all,radio_archived,radio_not_archived,menu,user_menu,user_icon])
        for element in result:
            if element == False:
                return False
        return True


    def radio_btns_active_msg(self):
        self.waitForElement(locator=self.locator['radio_not_archived'], locatorType='id')
        self.elementClick(locator=self.locator['radio_not_archived'], locatorType='id')
        active_msg = self.getElementlist(locator=self.locator['msg_list'], locatorType='xpath')
        action_check = []
        for element in active_msg:
            element_id = element.get_attribute("id")
            archive_action_locator = "//div[@id='"+element_id+"']//i[@data-tpe='archiveMsgAction']"
            check_archive_btn = self.isElementDisplayed(locator=archive_action_locator, locatorType='xpath')
            action_check.append(check_archive_btn)
            for result in action_check:
                if result == False:
                    return result
            return result


    def radio_btns_archived_msg(self):

        self.elementClick(locator=self.locator['radio_archived'], locatorType='id')
        self.waitForElement(locator=self.locator['archived_msg'], locatorType='xpath')
        msg = self.getElementlist(locator=self.locator['archived_msg'], locatorType='xpath')
        action_check = []
        for element in msg:
            element_id = element.get_attribute("id")
            archive_action_locator = "//div[@id='" + element_id + "']//i[@data-tpe='archiveMsgAction']"
            check_archive_btn = self.isElementDisplayed(locator=archive_action_locator, locatorType='xpath')
            action_check.append(check_archive_btn)
            for result in action_check:
                if result == False:
                    result = True
                    return result
                else:
                    return False


    def radio_btns_all_msg(self):
        self.waitForElement(locator=self.locator['radio_all'], locatorType='id')
        self.elementClick(locator=self.locator['radio_all'], locatorType='id')
        self.waitForElement(locator=self.locator['all_msg_list'], locatorType='xpath')
        time.sleep(2)
        msg_all = self.getElementlist(locator=self.locator['all_msg_list'], locatorType='xpath')
        #get number of active msg
        self.elementClick(locator=self.locator['radio_not_archived'], locatorType='id')
        self.waitForElement(locator=self.locator['msg_list'], locatorType='xpath')
        time.sleep(2)
        msg = self.getElementlist(locator=self.locator['msg_list'], locatorType='xpath')
        #get number of archived msg
        self.elementClick(locator=self.locator['radio_archived'], locatorType='id')
        self.waitForElement(locator=self.locator['archived_msg'], locatorType='xpath')
        msg_archived = self.getElementlist(locator=self.locator['archived_msg'], locatorType='xpath')
        if len(msg_all) == len(msg) + len(msg_archived):
            return True
        else:
            return False

    def mark_as_read_action(self):
        # get id and title active unread msg
        self.elementClick(locator=self.locator['radio_not_archived'])
        unread_msg_id = self.get_unread_msg_id()
        if unread_msg_id != None:
            unread_msg_id.lstrip('msg')
            mark_as_read_locator = "//i[@id='readedMsgAction"+unread_msg_id+"']"
            self.elementClick(locator=mark_as_read_locator, locatorType='xpath')
            tm.sleep(3)
            # check if action is not ready
            check_presence = self.isElementPresent(locator=mark_as_read_locator, locatorType='xpath')
            if check_presence == False:
                return True
            else:
                return False
        else:
            return None

    def mark_archived_action(self):
        # get id of the first msg
        msg_id = self.get_unread_msg_id().lstrip('msg')
        archived_action_locator = "//i[@id='archiveMsgAction"+msg_id+"']"
        self.elementClick(locator=archived_action_locator, locatorType='xpath')
        tm.sleep(3)
        # check if action is not ready
        archived_action_check_presence = self.isElementPresent(locator=archived_action_locator, locatorType='xpath')
        # go to archived view
        if archived_action_check_presence == False:
            return True
        else:
            return False

    def check_details_unreaded_msg(self):
        self.clearField(locator=self.locator['search_window'], locatorType='css')
        self.elementClick(locator=self.locator['msg_btn_clear'], locatorType='id')
        self.waitForElement(locator=self.locator['radio_not_archived'], locatorType='id')
        self.elementClick(locator=self.locator['radio_not_archived'], locatorType='id')
        msg_id = str(self.get_unread_msg_id())
        id_number = msg_id.lstrip('msg-')
        msg_back_action = "//div[@class='close-btn']//i[@data-tpe='msg-back']"
        archived_action = "//div[@class='header-toolbar']//i[@id='archiveMsgAction-"+id_number+"']"
        mark_readed_action = "//div[@class='header-toolbar']//i[@id='readedMsgAction-"+id_number+"']"
        self.waitForElement(locator=msg_id, locatorType='id', pollFrequency=1)
        self.elementClick(locator=msg_id, locatorType='id')
        self.waitForElement(self.locator['msg_back_action'], locatorType='xpath', pollFrequency=1)
        self.isElementDisplayed(locator=self.locator['msg_back_action'], locatorType='xpath')
        self.isElementDisplayed(locator=self.locator['archived_action'], locatorType='xpath')
        self.isElementDisplayed(locator=self.locator['mark_readed_action'], locatorType='xpath')





