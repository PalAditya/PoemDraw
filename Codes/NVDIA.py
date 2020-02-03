from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import logging
import time
import random
logging.basicConfig(level=logging.DEBUG)

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
website_URL ="http://34.216.122.111/gaugan/"
url = driver.get(website_URL) 
for i in range(10):
	try:
		driver.find_element_by_id("myCheck").click()
		fileInput = driver.find_element_by_id("realfile")
		namearray = ["l","m"]
		fileName = random.randint(0,1)
		toGAUGAN = input()
		if int(toGAUGAN) == 2:
			namearray[fileName] = "n"
		fileInput.send_keys("E:\\BTP\Codes\\"+namearray[fileName]+".png")
		driver.find_element_by_id("btnRealLoad").click()
		time.sleep(3)
		driver.find_element_by_id("render").click()
		break
	except NoSuchElementException as e:
		print('retry in 1s.')
		time.sleep(1)
else:
	raise NoSuchElementException