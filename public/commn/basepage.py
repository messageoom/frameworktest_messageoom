#coding=utf-8
__author__ = 'Kal-W'

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
            self.logger.info('############################### START ###############################')
            self.msDriver = webdriver.Chrome(executable_path = globalparam.chromedriverpath)
            time.sleep(1)
            self.msDriver.maximize_window()

        except Exception:
            self.logger.info("======>Could not open the browser correctly. Please check if the browser driver is installed")
        else:

            self.logger.info('======>Successfully launched the browser')
#            return self.msDriver


    def tearDown(self):
        self.msDriver.quit()
        self.logger.info('################################ End ################################')
"""
    def test_mytest(self):
        try:
            self.msDriver.get(globalparam.base_url + "/login")
            time.sleep(0.5)
            self.msDriver.find_element_by_name("username").clear()
            self.msDriver.find_element_by_name("username").send_keys("admin-wlzx")
            self.msDriver.find_element_by_name("password").clear()
            self.msDriver.find_element_by_name("password").send_keys("123456")

            self.msDriver.find_element_by_xpath("//button[@type='subumit']").click()
            time.sleep(2)
#    myloger.info("{0}-----登录成功-----{1}".format(success,test01))

        except WebDriverException:
            print "登录失败"
        else:
            print "登录成功"
"""


