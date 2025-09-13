import smtplib

my_email = "jettie.friesen@ethereal.email"
password = "jhGjS6jQjB3PxJmN3t"

# for connecting use gmail provider
with smtplib.SMTP("smtp.ethereal.email", port=587) as connection:

    # for securing the connection to the email server
    connection.starttls()

    connection.login(user=my_email, password =password)

    msg = "Subject: Test Email\n\nHello, this is a test message from Python!"
    try:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=msg
        )
    except Exception as error_message:
        print("Email was not Sent")
    else:
        print("Email was Sent!")