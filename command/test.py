import time
from base import CommandBase
from util.project_web_driver import ProjectWebDriver

from setting import SELENIUM_WEB_DRIVER_PATH, URL_BASE


class Command(CommandBase):

    def __init__(self):
        super(Command, self).__init__(description="テスト")
        self.driver = ProjectWebDriver(SELENIUM_WEB_DRIVER_PATH, URL_BASE)


    def handle(self):
        self.driver.search("docker selenium")
        self.driver.close()


command = Command()
command.run()
