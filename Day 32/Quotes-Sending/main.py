import datetime as dt
import smtplib, random

my_email = "lucius73@ethereal.email"
password = "rXfG29PJQKJy7B614V"

now = dt.datetime.now()
minutes = now.minute
min_list = list(str(minutes))

with open("quotes.txt", mode = "r") as file:
    content = file.readlines()
    quote = random.choice(content)

if min_list[1] == "0":
    try:
        with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)

            message = f"Subject: Motivation for Dose\n\n{quote}"
            try:
                connection.sendmail(
                    from_addr = my_email,
                    to_addrs= my_email,
                    msg = message
                )
            except Exception :
                print(f"Mail was not Delievered,{Exception}")
            else:
                print("Mail Sent!")
    except Exception :
        print("Connection was not established")
