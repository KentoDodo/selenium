import unittest
from util.project_web_driver import ProjectWebDriver

from setting import SELENIUM_WEB_DRIVER_PATH, URL_BASE


class TestProject(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = ProjectWebDriver(SELENIUM_WEB_DRIVER_PATH, URL_BASE)


    @classmethod
    def tearDownClass(self):
        self.driver.close()


    def test_search(self):
        expected = "query: qawsedrftgyhujikolp"
        actual = self.driver.search("qawsedrftgyhujikolp")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
