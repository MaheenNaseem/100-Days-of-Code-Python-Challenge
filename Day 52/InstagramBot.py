from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

load_dotenv()
SIMILAR_NAME = "tesoro.pk"
EMAIL= os.getenv("INSTAGRAM_EMAIL")
PASSWORD =os.getenv("INSTAGRAM_PASSWORD")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.wait = WebDriverWait(self.driver, 10)

    def _login(self):
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys(EMAIL, Keys.ENTER)

        password = self.driver.find_element(By.NAME, 'pass')
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(3)

        try:
            not_now_save_info = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))
            not_now_save_info.click()
            time.sleep(1)
        except:
            pass

        try:
            not_now_notification = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            not_now_notification.click()
        except:
            pass


    def find_followers(self):

        self.driver.get(f"https://www.instagram.com/{SIMILAR_NAME}/")
        time.sleep(3)

        try:
            followers_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]")))

        except:
            followers_tab = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'followers')]/ancestor::a")))

        followers_tab.click()
        time.sleep(3)

    def follow(self):
        try:
            print("Entering follow")
            popup = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='dialog']")))
            # scroll_box = popup.find_element(By.XPATH, ".div[contains(@style, 'overflow')]")

            for items in range(5):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
                time.sleep(2)
                try:
                    follow_buttons = popup.find_elements(By.XPATH, "//button")
                    print(f"Found {len(follow_buttons)} buttons")
                    for button in follow_buttons:
                        try:
                            if button.text in ["Follow", "Follow Back"]:
                                button.click()
                                time.sleep(2)
                        except:
                            print('Follow not clicked')

                except:
                    print(f"No follow buttons found on scroll {items + 1}")

        except Exception as e:
            print(f"Error in follow: {e}")
instabot = InstaFollower()
try:
    instabot._login()
    instabot.find_followers()
    instabot.follow()
except Exception as e:
    print(f"An error occurred: {e}")

