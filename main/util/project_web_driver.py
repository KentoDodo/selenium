import time

from util.selenium_web_driver import SeleniumWebDriver
from selenium.webdriver.common.keys import Keys


class ProjectWebDriver(SeleniumWebDriver):

    def search(self, query):
        # do search
        self.driver.find_element_by_css_selector("input[name='query']").send_keys(str(query))
        self.driver.find_element_by_css_selector("#query_submit").send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)
        return self.get_search_result()


    def get_search_result(self):
        return self.driver.find_element_by_css_selector("#sent_params").text
