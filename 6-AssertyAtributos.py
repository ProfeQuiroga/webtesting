import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

class Asserts_Examples(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_assert_form(self):
        driver = self.driver
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

        first_name = driver.find_element_by_name("firstname")
        first_name.send_keys("Martina")
        assert first_name.get_attribute('value') == 'Martina'
        #assert first_name.get_attribute('value') == 'Martin'
        assert "Martin" in first_name.get_attribute('value')
        time.sleep(3)

        continentes = Select(driver.find_element_by_id("continents"))
        continentes.select_by_index(2)
        assert continentes.first_selected_option.get_attribute('value') == 'Africa' 
        time.sleep(3)

        radio = driver.find_element_by_id("sex-0")
        print(radio.get_attribute('checked'))
        radio.click()
        assert radio.get_attribute('checked') == 'true'
        time.sleep(3)

        check = driver.find_element_by_id("profession-0")
        check.click()
        assert check.get_attribute('checked') == 'true'
        time.sleep(3)

    def test_assert_yahoo(self):
        driver = self.driver
        driver.get("https://login.yahoo.com/")
        username = driver.find_element_by_id("login-username")
        username.send_keys("nodebeexistir")
        assert driver.find_element_by_id("username-error").is_displayed() == False
        username.send_keys(Keys.ENTER)
        time.sleep(3)
        assert driver.find_element_by_id("username-error").is_displayed() == True
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
