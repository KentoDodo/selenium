import time
from base import CommandBase
from util.driver_base import DriverBase
from selenium.webdriver.common.keys import Keys

from setting import SELENIUM_WEB_DRIVER_PATH, URL_BASE


class Command(CommandBase):

    def __init__(self):
        super(Command, self).__init__(description="テスト")
        self.driver = DriverBase(SELENIUM_WEB_DRIVER_PATH, URL_BASE)


    def handle(self):
        self.search("docker selenium")
        self.close()


    def search(self, query):
        # do search
        self.driver.driver.find_element_by_css_selector("input[name='q']").send_keys(str(query))
        self.driver.driver.find_element_by_css_selector("input[name='q']").send_keys(Keys.RETURN)
        time.sleep(self.driver.sleep_second)


    def close(self):
        self.driver.driver.close()


command = Command()
command.run()
