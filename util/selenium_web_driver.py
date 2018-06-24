import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumWebDriver(object):

    def __init__(self,driver_path, url_base, desired_capabilities=DesiredCapabilities.CHROME, sleep_second=0):
        self.driver_path = driver_path
        self.url_base = url_base
        self.sleep_second = sleep_second
        self.desired_capabilities = desired_capabilities
        self.driver = self._get_new_webdriver()
        self._to_top()


    def _get_new_webdriver(self):
        # connection
        return webdriver.Remote(
            command_executor=self.driver_path,
            desired_capabilities=self.desired_capabilities
        )


    def _to_top(self):
        # jump to top page
        self.driver.get(self.url_base)
        time.sleep(self.sleep_second)


    def close(self):
        # close
        self.driver.close()
        self.driver.quit()
        time.sleep(self.sleep_second)
