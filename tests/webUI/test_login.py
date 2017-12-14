#coding=utf-8
__author__ = 'messageoom'

import time

from selenium.common.exceptions import WebDriverException

from config import globalparam
from public.selenium_base import basepage


class TestLogin(basepage.BasePage):

    def test_mytest(self):

        try:
            self.msDriver.get(globalparam.base_url + "/login")
            time.sleep(1)
            self.msDriver.find_element_by_name("username").clear()
            self.msDriver.find_element_by_name("username").send_keys("admin-wlzx")
            self.msDriver.find_element_by_name("password").clear()
            self.msDriver.find_element_by_name("password").send_keys("123456")
            self.msDriver.find_element_by_css_selector("[type='submit']").click()

            time.sleep(1)
        except WebDriverException:
            self.logger.info("[Failed]")
        else:
            self.logger.info("[successful]")

#    myloger.info("{0}-----登录成功-----{1}".format(success,test01))