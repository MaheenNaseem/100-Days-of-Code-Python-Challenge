from IPython.core.completerlib import import_re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

EMAIL= "test@gmail.com"
PASSWORD= "" #your password here
URL="https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)
driver.get(URL)

# create a directory in your project folder to store your Chrome Profile information
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# Tell your Chrome Driver to use the directory you specified to store a "profile"
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")




