import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

class Options(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_select(self):
        driver = self.driver
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        continentes = Select(driver.find_element_by_id("continents"))
        continentes.select_by_visible_text("Europe")
        time.sleep(3)
        continentes.select_by_index(3)
        time.sleep(3)

    def test_radioButton(self):
        driver = self.driver
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        radio = driver.find_element_by_id("sex-0")
        radio.click()
        time.sleep(3)
        radio = driver.find_element_by_id("sex-1")
        radio.click()
        time.sleep(3)

    def test_checkBox(self):
        driver = self.driver
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        check = driver.find_element_by_id("profession-0")
        check.click()
        time.sleep(3)
        check = driver.find_element_by_id("profession-1")
        check.click()
        time.sleep(3)
               
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
