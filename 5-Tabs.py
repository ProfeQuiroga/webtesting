import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Tabs(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_tabs(self):
		driver = self.driver
		driver.get("https://python.org")
		time.sleep(2)
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[1])
		driver.get("https://google.com")
		elem = driver.find_element_by_name("q")
		elem.send_keys("unsj")
		elem.send_keys(Keys.ENTER)
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)
		download = driver.find_element_by_xpath("//*[@id='content']/div/section/div[1]/div[2]/p[2]/a")
		download.click()
		time.sleep(3)
		driver.back()
		time.sleep(3)
		driver.forward()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
