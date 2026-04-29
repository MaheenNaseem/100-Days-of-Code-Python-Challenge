from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

EMAIL = "TEST@gmail.com"
PASSWORD = "YOUR PASSWORD HERE"
URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# wait for elements to load
driver.implicitly_wait(5)

login_btn = driver.find_element(By.ID, 'login-button')
login_btn.click()

driver.implicitly_wait(2)

email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(EMAIL)

password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(PASSWORD)

submit_btn = driver.find_element(By.ID, 'submit-button')
submit_btn.click()