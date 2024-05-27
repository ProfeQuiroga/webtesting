import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class FindElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_w3schools_com(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/xml/xpath_syntax.asp")
        lupa = driver.find_element_by_xpath("//*[@id='topnav']/div/div[1]/a[15]")
        lupa.click()
        buscar = driver.find_element_by_id("gsc-i-id1")
        buscar.send_keys("python")
        time.sleep(3)
        buscar.clear()
        buscar = driver.find_element_by_name("search")
        buscar.send_keys("php")
        time.sleep(3)
        equis = driver.find_element_by_xpath("//*[@id='topnav']/div/div[1]/a[15]")
        equis.click()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
