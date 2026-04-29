from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

EMAIL = "test@gmail.com"
PASSWORD = "your password here"
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

day= "Tue"
time = "6:00 PM"

day_groups = driver.find_elements(By.CSS_SELECTOR, value='div[id^=day-group]')

for groups in day_groups:
    current_day = groups.find_element(By.CSS_SELECTOR, value='.Schedule_dayTitle__YBybs').text
    date = ((current_day.split())[-1]).strip(")")

    if day in current_day:
        all_classes_cards = groups.find_elements(By.CSS_SELECTOR, value="div[id^='class-card']")

        for classes in all_classes_cards:
            available_time = classes.find_element(By.CSS_SELECTOR, value="p[id^='class-time-']").text

            if time in available_time:
                class_title = classes.find_element(By.CSS_SELECTOR, value="h3[id^='class-name-']").text
                btn_available = classes.find_element(By.CSS_SELECTOR, value= "button[id^='book-button-']")
                btn_available.click()

                action_text = btn_available.text
                value= action_text
                match value:
                    case "Booked":
                        result = "Already booked"
                    case "Waitlisted":
                        result = "Already on waitlist"
                    case "Join Waitlist":
                        result= "Joined waitlist for"

                print(f"✓ {result}: {class_title} on {day},{date}")

driver.quit()