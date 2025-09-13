# To run the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Update the SMTP ADDRESS to match your my_email provider.
# 3. Update birthdays.csv to contain today's month and day.

import random, smtplib, pandas
import datetime as dt

my_email = "lucius73@ethereal.my_email"
my_password = "rXfG29PJQKJy7B614V"

# get today's date and month
now = dt.datetime.now()
today = (now.month, now.day)

# read csv
birthdays = pandas.read_csv("birthdays.csv")

# iterate over csv
for (index, row) in birthdays.iterrows():

    # Check if today matches a birthday in the birthdays.csv
    if (row["month"], row["day"]) == today:

        # generate a random number and use that to select 1/3 letter
        num = random.randint(1, 3)
        letter_file = f"letter_templates/letter_{num}.txt"

        # open selected file
        with open(letter_file, mode="r") as file:
            wish = file.read()

        # replace the name with the birthday person's name
        wish = wish.replace("[NAME]", row["name"])

        # establish connection
        with smtplib.SMTP("smtp.ethereal.my_email", 587) as connection:
            connection.starttls()
            # sending mail
            try:
                connection.login(my_email, my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row["email"],
                    msg=f"Subject: Happy Birthday!!!\n\n{wish}"
                )
            except smtplib.SMTPException as e:
                print("Mail Not Sent!", e)
            else:
                print("Mail Sent")