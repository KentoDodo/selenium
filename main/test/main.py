import unittest
import copy, csv
from datetime import datetime
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
        """description of this test"""
        expected = "query: qawsedrftgyhujikolp"
        actual = self.driver.search("qawsedrftgyhujikolp")

        result = self.assertEqual(expected, actual)


    def test_search_failure(self):
        """description of this test 'failure'"""
        expected = "query: hoge"
        actual = self.driver.search("failure")

        result = self.assertEqual(expected, actual)


    def test_search_error(self):
        """description of this test 'error'"""
        expected = "query: hoge"
        actual = self.driver.searchs("failure")

        result = self.assertEqual(expected, actual)


    def test_search_skip(self):
        """description of this test 'skip'"""
        self.skipTest("This is skip test")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProject)
    _suite = copy.deepcopy(suite)

    test_runner = unittest.TextTestRunner().run(_suite)

    suite_errors_ids = [s[0].id() for s in test_runner.errors]
    suite_failures_ids = [s[0].id() for s in test_runner.failures]
    suite_skipped_ids = [s[0].id() for s in test_runner.skipped]

    csv_path = 'log/test_result/test_%s.csv' % (datetime.now().strftime("%Y%m%d%H%M%S"))
    f = open(csv_path, 'w')
    writer = csv.writer(f, lineterminator='\n')
    for s in suite:
        result_text = "OK"
        if s.id() in suite_errors_ids:
            result_text = "ERROR"
        if s.id() in suite_failures_ids:
            result_text = "FAIL"
        if s.id() in suite_skipped_ids:
            result_text = "SKIP"
        writer.writerow([s.shortDescription(), result_text])
    f.close()
    print("output result to %s" % (csv_path))
