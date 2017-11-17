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






"""
def getElement_longin():

    driver = publicVariable.publicDriver
    driver.maximize_window()
    driver.get(publicVariable.loginUrl)
    print driver.title
    sleep(1)
#    driver.set_window_size(100,100)
    driver.find_element_by_name('username').send_keys('xxxxx')
    driver.find_element_by_name('password').send_keys('xxxxx')
    driver.find_element_by_css_selector("button[type='submit']").click()
#    driver.find_element_by_css_selector(".btn.btn-primary.block.full-width.m-b").click()
#    driver.find_element_by_css_selector("[type='submit']").click()

#    driver.get(publicVariable.reviewUrl)
#    driver.find_element_by_css_selector("[href='http://merchants.guxiansheng.cn/wlzx/comment/reply?id=220&status=1&type=1']").click()
#    return
    driver.find_element_by_link_text(u"内容管理").click()
    sleep(1)
    driver.find_element_by_link_text(u"服务包").click()
    sleep(1)
    driver.get(publicVariable.testurl)
    driver.find_element_by_xpath(u"(//a[contains(text(),'查看内容')])[3]").click()
    #driver.find_element_by_xpath("/html/body/div[2]/div/form/div/table/tbody/tr[3]/td[9]/span[2]/a").click()
    driver.find_element_by_link_text(u"新增标的").click()
    driver.find_element_by_name("service_title").click()
    driver.find_element_by_name("service_title").clear()
    driver.find_element_by_name("service_title").send_keys(u"消息标题")
    driver.find_element_by_name("service_describe").clear()
    driver.find_element_by_name("service_describe").send_keys(u"文章描述")
    driver.find_element_by_id("select2-sel_menu2-container").click()
    driver.find_element_by_css_selector("[role='textbox']").send_keys("000001")
    driver.find_element_by_css_selector("[role='treeitem']").click()
    #driver.find_element_by_css_selector("span.select2-selection__placeholder").click()
    driver.find_element_by_id("add_role").click()
#    driver.find_element_by_name("first_buying_rate").clear()
    element = driver.find_element_by_css_selector("[name='now_price']")
    sleep(1)
    # Get the price of the current stock
    now_price = element.get_attribute("value")
    myUtils = utils.Utils().limit_price(float(now_price))

    driver.find_element_by_name("first_buying_rate").send_keys("%s" % myUtils[2])
    driver.find_element_by_name("second_selling_rate").clear()
    driver.find_element_by_name("second_selling_rate").send_keys("%s" % myUtils[3])
    driver.find_element_by_name("fist_win_rate").clear()
    driver.find_element_by_name("fist_win_rate").send_keys("%s" % myUtils[4])
    driver.find_element_by_name("second_win_rate").clear()
    driver.find_element_by_name("second_win_rate").send_keys("%s" % myUtils[5])
    driver.find_element_by_name("fist_lose_rate").clear()
    driver.find_element_by_name("fist_lose_rate").send_keys("%s" % myUtils[6])
    driver.find_element_by_name("second_lose_rate").clear()
    driver.find_element_by_name("second_lose_rate").send_keys("%s" % myUtils[7])
    driver.find_element_by_name("plan_rate").clear()
    driver.find_element_by_name("plan_rate").send_keys("5")

    driver.find_element_by_css_selector("div.col-sm-9 > input[name=\"service_marketanalysis_name\"]").clear()
    driver.find_element_by_css_selector("div.col-sm-9 > input[name=\"service_marketanalysis_name\"]").send_keys(u"宏观概括标题")
    driver.find_element_by_css_selector("div.col-sm-9 > textarea[name=\"service_marketanalysis\"]").clear()
    driver.find_element_by_css_selector("div.col-sm-9 > textarea[name=\"service_marketanalysis\"]").send_keys(u"宏观概括类容")
    driver.find_element_by_css_selector("div.col-sm-9 > input[name=\"service_sectoranalysis_name\"]").clear()
    driver.find_element_by_css_selector("div.col-sm-9 > input[name=\"service_sectoranalysis_name\"]").send_keys(u"行业动态标题")
    driver.find_element_by_css_selector("div.col-sm-9 > textarea[name=\"service_sectoranalysis\"]").clear()
    driver.find_element_by_css_selector("div.col-sm-9 > textarea[name=\"service_sectoranalysis\"]").send_keys(u"行业动态类容")
    driver.find_element_by_xpath("/html/body/div[3]").send_keys(Keys.DOWN)
    driver.find_element_by_css_selector("[class='phpdebugbar-close-btn']").click()
#    driver.find_element_by_id("myModal").send_keys(Keys.UP)
    driver.find_element_by_css_selector("div.modal-footer > button[type='submit']").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[6]/div[4]/div[3]/div/input").send_keys("5")
#    driver.find_element_by_css_selector("div.col-sm-5 > input[name=\"max_rate_days\"]").send_keys("5")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[7]/div/input").click()

#getElement_longin()

"""