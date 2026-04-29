from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import os
# teset233

EMAIL = "test@gmail.com"
PASSWORD = "t3$t_123"
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

day_targets = ['Tue', 'Thu']
target_time = '6:00 PM'

booked = 0
waitlisted = 0
already_done = 0

processed_classes = []
# ---------------- SCRAPE ----------------
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    current_day = day_group.find_element(By.CSS_SELECTOR, ".Schedule_dayTitle__YBybs").text

    if any(day in current_day for day in day_targets):
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

        if target_time in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            class_info = f"{class_name} on {current_day}"
            state = button.text.lower().strip()

            if state == "booked":
                print(f"✓ Already booked: {class_info}")
                already_done += 1
                processed_classes.append(f"[Booked] {class_info}")

            elif state == "waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_done += 1
                processed_classes.append(f"[Waitlisted] {class_info}")

            elif state == "book class":
                button.click()
                print(f"✓ Successfully booked: {class_info}")
                booked += 1
                processed_classes.append(f"[New Booking] {class_info}")

            elif state == "join waitlist":
                print(f"✓ Joined waitlist for: {class_info}")
                already_done += 1
                processed_classes.append(f"[New Waitlist] {class_info}")

#  Step 06 - printing statement
# print(f'''\n------BOOKING SUMMARY------
# Classes Booked: {booked}
# Waitlists joined: {waitlisted}
# Already booked/waitlisted: {already_done}
# Total Tuesday & Thursday 6pm  classes processed: {booked+waitlisted+already_done}
# ''')
#
# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")

#  step 07:

total_booking = already_done+waitlisted+booked
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booking} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_booking_btn = driver.find_element(By.CSS_SELECTOR , value="#my-bookings-link")
my_booking_btn.click()

driver.implicitly_wait(10)

verified_count = 0

all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booking} bookings")
print(f"Found: {verified_count} bookings")

if total_booking == verified_count:
    print("SUCCESS: All bookings verified!")
else:
    print(f"MISMATCH: Missing {total_booking - verified_count} bookings")


driver.quit()