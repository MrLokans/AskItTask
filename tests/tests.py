import os

import unittest

from selenium import webdriver

BASE_PROJECT_DIR = os.path.abspath(os.path.normpath('..'))


class TestTasksApp(unittest.TestCase):

    def setUp(self):
        self.main_page = os.path.join(BASE_PROJECT_DIR, "index.html")
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_page_has_proper_title(self):
        print self.main_page
        self.browser.get(self.main_page)
        self.assertIn("AskItTask", self.browser.title)


if __name__ == '__main__':
    unittest.main()
