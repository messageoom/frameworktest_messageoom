#coding=utf-8
__author__ = 'Kal-W'

from mCase import test_login
from time import sleep
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common.keys import Keys


class TestPostArticle(test_login.TestLogin):

    def test_post_article(self):

        try:
            self.msDriver.find_element_by_link_text(u"内容管理").click()
            sleep(1)
            self.msDriver.find_element_by_link_text(u"服务包").click()

            sleep(1)
        except WebDriverException:
            self.logger.info("[Failed]")
        else:
            self.logger.info("[successful]")