from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
website_URL ="http://nvidia-research-mingyuliu.com/gaugan/"
url=driver.get(website_URL) 
print(url)
landscape = driver.find_element_by_class_name('btncat cat-landscape')
landscape.send_keys(Keys.ENTER)
mountain = driver.find_element_by_class_name('lbl-mountain')
mountain.send_keys(Keys.ENTER);