#coding=utf-8
__author__ = 'messageoom'

import time
import unittest
from selenium import webdriver
from config import globalparam
from public.commn.log import Log
from selenium.common.exceptions import WebDriverException

class BasePage(unittest.TestCase):
    """
    This is a base page class for Page Object.
    """
    def setUp(self):

        try:
            self.logger = Log()
            self.logger.info('Start to execute: (%s)\n'%time.strftime('%Y-%m-%d %H:%M:%S',
                                                                      time.localtime(time.time())))
            self.msDriver = webdriver.Chrome(executable_path = globalparam.chromedriverpath)
            time.sleep(1)
            self.msDriver.maximize_window()

        except Exception as e:
            self.logger.info("Could not open the browser correctly. Please check if the browser driver is installed !")
            raise e
        else:

            self.logger.info('Successfully launched the browser !')
#            return self.msDriver


    def tearDown(self):
        self.msDriver.quit()
        self.logger.info('End to execute: (%s)\n'%time.strftime('%Y-%m-%d %H:%M:%S',
                                                                  time.localtime(time.time())))

