from email import message_from_string

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib
load_dotenv()

SMTP_ADDRESS=os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6/ref=sr_1_1?crid=20A3BWWJEOBHT&dib=eyJ2IjoiMSJ9.vowf1RIH8cKd6FHI2bA3tOQlloUh9Zv6oxForzJxA34jGB8niMxRedezeGwndsfPHlb3PdZJwEEJFvrdL65ABbNrhJC1TCnntN26GLl1CGsQ_K0l92cetatY7BLTcmo-wXdLVLt8tXkl9BR94hXNatAxPp0CdZ5T94pNTn0A7TKXL-fkhFTIc0vDYVjGu8vx22SnbqTs9EUMxyUa_249bnluFqHBCnQ8_iwdryzygD8.7ilfpQt8OjnIOddZ04h3P3UGiOaI0mLMr_atulJ_cDc&dib_tag=se&keywords=Instant%2BPot%2BDuo%2BPlus%2B9-in-1%2BElectric%2BPressure%2BCooker%2C%2BSlow%2BCooker%2C%2BRice%2BCooker%2C%2BSteamer%2C%2BSaut%C3%A9%2C%2BYogurt%2BMaker%2C%2BWarmer%2B%26%2BSterilizer%2C%2BIncludes%2BApp%2BWith%2BOver%2B800%2BRecipes%2C%2BStainless%2BSteel%2C%2B3%2BQuart&nsdOptOutParam=true&qid=1777391219&sprefix=%2Caps%2C362&sr=8-1&th=1"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers)
context = response.text

soup = BeautifulSoup(context, 'html.parser')
item_name=((soup.find(name='span', id="productTitle")).getText()).strip()
price = (soup.find(name= 'span', class_="a-offscreen")).getText()

price_float= float((price.split('$'))[1])
print(f"Item: {item_name}")
print(f"Price: {price_float}")

with smtplib.SMTP(SMTP_ADDRESS,587) as connection:
    connection.starttls()
    connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

    message = (f"Subject: Amazon Price Alert\n\n"
               f"{item_name} now ${price_float}\n {url}")

    try:
        connection.sendmail(
            from_addr= EMAIL_ADDRESS,
            to_addrs= "receiver@gmail.com",
            msg = message.encode('utf-8')
        )
    except smtplib.SMTPException as e:
        print(f"Mail couldn't be delivered {e}")
    else:
        print("Mail was delivered")