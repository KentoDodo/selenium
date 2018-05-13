from base import CommandBase
from util.driver_base import DriverBase


class Command(CommandBase):

    def __init__(self):
        super(Command, self).__init__(description="テスト")


    def handle(self):
        driver = DriverBase()
        driver.search("docker selenium")
        driver.close()


command = Command()
command.run()
