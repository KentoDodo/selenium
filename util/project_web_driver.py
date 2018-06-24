import time

from util.selenium_web_driver import SeleniumWebDriver
from selenium.webdriver.common.keys import Keys


class ProjectWebDriver(SeleniumWebDriver):

    def search(self, query):
        # do search
        self.driver.find_element_by_css_selector("input[name='q']").send_keys(str(query))
        self.driver.find_element_by_css_selector("input[name='q']").send_keys(Keys.RETURN)
        time.sleep(self.sleep_second)
