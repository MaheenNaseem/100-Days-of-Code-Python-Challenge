from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(5)

try:
    driver.find_element(By.ID, "langSelect-EN").click()
except NoSuchElementException:
    pass

time.sleep(2)

cookie_button = driver.find_element(By.ID, "bigCookie")

def cookie_count():
    text = driver.find_element(By.ID, "cookies").text
    cookies = text.split(" ")[0].replace(",", "")
    return int(cookies)

def buy_upgrade():
    items = driver.find_elements(By.CSS_SELECTOR, "#products .product.unlocked.enabled")

    for item in reversed(items):
        try:
            price = item.find_element(By.CLASS_NAME, "price").text
            price = int(price.replace(",", ""))

            if cookie_count() >= price:
                try:
                    item.click()
                    break
                except ElementClickInterceptedException:
                    try:
                        banner = driver.find_element(By.CLASS_NAME, "cc_banner")
                        driver.execute_script("arguments[0].remove();", banner)
                        item.click()
                        break
                    except:
                        pass
        except:
            continue


check_time = time.time() + 5

while True:
    cookie_button.click()

    if time.time() > check_time:
        buy_upgrade()
        check_time = time.time() + 5