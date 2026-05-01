from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP= 50
TWITTER_EMAIL= os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD= os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_argument("--disable-geolocation")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.geolocation": 2,  # 2 means block
        })
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        self.driver = webdriver.Chrome(options=chrome_options)

        # Mask the webdriver property that Twitter checks
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self.up=0
        self.down=0

    def slow_type(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.1)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        wait = WebDriverWait(self.driver, 30)
        go_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_button.click()
        print("Speed test started...")

        time.sleep(30)

        download_speed = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        self.down = float(download_speed.text)
        print(f"Download: {self.down}")

        time.sleep(30)

        upload_speed = wait.until(EC.presence_of_element_located((By.XPATH,  '//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        self.up = float(upload_speed.text)
        print(f"Upload: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)

        email = wait.until(EC.element_to_be_clickable((By.NAME, "text")))
        email.click()
        self.slow_type(email, TWITTER_EMAIL)
        time.sleep(0.5)
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        print("URL after email:", self.driver.current_url)
        print("Page title:", self.driver.title)

        # Step 2: Username verification (if prompted)
        try:
            verification_field = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
            self.slow_type(verification_field, TWITTER_USERNAME)
            time.sleep(0.5)
            verification_field.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            print("No username verification needed")

        # Step 3: Password
        password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        password.click()
        self.slow_type(password, TWITTER_PASSWORD)
        time.sleep(0.5)
        password.send_keys(Keys.ENTER)
        print("Logged in!")

bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()