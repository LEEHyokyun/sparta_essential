from selenium import webdriver

import unittest


class Functioan_test_Django(unittest.TestCase):
    def setUp(self):
        path = './chromedriver'
        self.driver = webdriver.Chrome(path)

    def test_has_worked_in_title(self):
        path = './chromedriver'
        driver = webdriver.Chrome(path)
        driver.get('http://localhost:8000')

        #assert "Django" in driver.title
        self.assertIn("worked", driver.title)

    def test_has_installed_in_title(self):
        path = './chromedriver'
        driver = webdriver.Chrome(path)
        driver.get('http://localhost:8000')

        # assert "Django" in driver.title
        self.assertIn("install", driver.title)