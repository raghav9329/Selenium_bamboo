'''
Created on 08.02.2017

@author: Ammar Najjar
'''
import unittest
import xmlrunner
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    url = "<PUT URL HERE>";
    driver = None;

    def setUp(self):
        self.driver = webdriver.Chrome();

    def tearDown(self):
        self.driver.close()

    def test_StartPage_title_contains_webshop(self):
        self.driver.get(self.url)
        title = self.driver.title
        self.assertIn("webshop", title)

    def test_Karten_link_existiert(self):
        self.driver.get(self.url)
        elem = self.driver.find_elements_by_css_selector("#mainNavigationBackground > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")
        self.assertIsNotNone(elem, "Karten Link is not found")

    def test_Artikel_link_existiert(self):
        self.driver.get(self.url)
        elem = self.driver.find_elements_by_css_selector("#mainNavigationBackground > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
        self.assertIsNotNone(elem, "Artikel Link is not found")

    def test_Abonnements_link_existiert(self):
        self.driver.get(self.url)
        elem = self.driver.find_elements_by_css_selector("#mainNavigationBackground > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)")
        self.assertIsNotNone(elem, "Abonnements Link is not found")

    def test_Geschenkgutscheine_link_existiert(self):
        self.driver.get(self.url)
        elem = self.driver.find_elements_by_css_selector("#mainNavigationBackground > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
        self.assertIsNotNone(elem, "Geschenkgutscheine Link is not found")

    def test_Mein_Konto_link_existiert(self):
        self.driver.get(self.url)
        elem = self.driver.find_elements_by_css_selector("#mainNavigationBackground > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
        self.assertIsNotNone(elem, "Mein_Konto Link is not found")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='nosetests'))
