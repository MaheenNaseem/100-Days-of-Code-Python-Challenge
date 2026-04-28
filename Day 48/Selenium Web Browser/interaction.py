from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# using simple click
total_article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a ")
# total_article_number.click()

# using link text
all_portals = driver.find_element(By.LINK_TEXT,value= "Content portals")
# all_portals.click()

# entering data in input field using send_keys method
search_bar= driver.find_element(By.NAME, value= 'search')

search_bar.send_keys("Python")
# error returned - reason screen size small, prevent by immediately maximizing screen or script the icon click and access input field from there

# for performing an action using keys we import keys from the selenium keys
search_bar.send_keys(Keys.ENTER)
