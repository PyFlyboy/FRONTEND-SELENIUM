
import configparser


def get_credentials():
    config = configparser.ConfigParser()
    config.read('..\\src\\base\\credentials.ini')
    return config

def get_locator():
    config = configparser.ConfigParser()
    config.read('..\\src\\base\\locators.ini')
    return config