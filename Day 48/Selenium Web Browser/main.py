from selenium import webdriver
from selenium.webdriver.common.by import By

#  to keep the window running using the web driver
chrome_options =webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org/")

# using x path would be parent element to time and name
events= driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

# use elements for the time and name
event_time = events.find_elements(By.CSS_SELECTOR, value= 'li time')
event_name= events.find_elements(By.CSS_SELECTOR ,value='a')

events_dict={}

# on the range of event time we set the time and name on the index of the event
for event in range(len(event_time)):
    events_dict[event]={
        'time':event_time[event].text,
        'name':event_name[event].text
    }

print(events_dict)


driver.quit()