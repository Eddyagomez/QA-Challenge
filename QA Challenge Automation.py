from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')

driver.get('http://automationpractice.com/index.php')

time.sleep(1)

nextPageBtn = driver.find_element_by_id("contact-link")
nextPageBtn.click()

time.sleep(1)

nextPageBtn = driver.find_element_by_id("id_contact")
nextPageBtn.click()

time.sleep(1)

drop = Select(nextPageBtn)

drop.select_by_visible_text("Customer service")

time.sleep(1)

nextPageBtn = driver.find_element_by_id("email")
nextPageBtn.click()

nextPageBtn.send_keys("eddyarturo@gmail.com")

time.sleep(1)

nextPageBtn = driver.find_element_by_id("id_order")
nextPageBtn.click()

nextPageBtn.send_keys("123456")

time.sleep(1)

nextPageBtn = driver.find_element_by_id("message")
nextPageBtn.click()

nextPageBtn.send_keys("Tengo un problema con mi orden.")

time.sleep(1)

nextPageBtn = driver.find_element_by_id("submitMessage")
nextPageBtn.click()

time.sleep(5)

driver.close()