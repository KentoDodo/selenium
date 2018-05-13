import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

from setting import SELENIUM_WEB_DRIVER_PATH, BASE_URL


class DriverBase(object):

    def __init__(self, sleep_second=5):
        self.SLEEP_SECOND = sleep_second
        self.driver = self._get_new_webdriver()
        self._to_top()


    def _get_new_webdriver(self):
        # connection
        return webdriver.Remote(
            command_executor=SELENIUM_WEB_DRIVER_PATH,
            desired_capabilities=DesiredCapabilities.CHROME
        )


    def _to_top(self):
        # jump to top page
        self.driver.get(BASE_URL)
        time.sleep(self.SLEEP_SECOND)


    def close(self):
        # close
        self.driver.close()
        self.driver.quit()
        time.sleep(self.SLEEP_SECOND)


    def search(self, query):
        # do search
        self.driver.find_element_by_css_selector("input[name='q']").send_keys(str(query))
        self.driver.find_element_by_css_selector("input[name='q']").send_keys(Keys.RETURN)
        time.sleep(self.SLEEP_SECOND)
        