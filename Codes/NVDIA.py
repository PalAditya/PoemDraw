from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
website_URL ="http://34.216.122.111/gaugan/"
url = driver.get(website_URL) 
for i in range(10):
	try:
		driver.find_element_by_id("myCheck").click()
		fileInput = driver.find_element_by_id("realfile")
		fileInput.send_keys("E:\\BTP\Codes\k.png")
		driver.find_element_by_id("btnRealLoad").click()
		time.sleep(3)
		driver.find_element_by_id("render").click()
		break
	except NoSuchElementException as e:
		print('retry in 1s.')
		time.sleep(1)
else:
	raise NoSuchElementException
# landscape = driver.find_element_by_id("myCheck").click()
# landscape.send_keys(Keys.ENTER)
# mountain = driver.find_element_by_class_name('lbl-mountain')
# mountain.send_keys(Keys.ENTER);