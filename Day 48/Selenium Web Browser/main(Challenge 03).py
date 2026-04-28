from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# getting elements
fname_field = driver.find_element(By.NAME, value= 'fName')
lname_field= driver.find_element(By.NAME, value='lName')
email_field = driver.find_element(By.NAME, value= 'email')

# Entering values
fname_field.send_keys('Aaron', Keys.TAB)
lname_field.send_keys('Warren',Keys.TAB)
email_field.send_keys("aaronWarner13@gmail.com", Keys.TAB, Keys.ENTER)

