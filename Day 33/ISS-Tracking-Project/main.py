import requests,  smtplib, time
import datetime as dt

my_email= "YOUR_EMAIL"
my_password= "YOUR PASSWORD"

# Your city's latitude and longitude
MY_LAT = ---
MY_LONG = ---

def iss_nearby():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    is_near = ((MY_LAT - 5) <= latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= longitude <= (MY_LONG + 5))

    if is_near:
        return True
    else:
        return False

def is_dark():
    parameter={
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }

    response_sun = requests.get(url=f"https://api.sunrise-sunset.org/json", params= parameter )
    response_sun.raise_for_status()
    data = response_sun.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+ 5
    sunset  = int(data["results"]["sunset"].split("T")[1].split(":")[0])+ 5

    # For current time_now
    now = dt.datetime.now()
    time_now = now.hour

    if time_now <= sunrise or time_now >= sunset:
        return True
    else:
        return False

while True:
    # checks if ISS is nearby and if it's dark
    if iss_nearby() and is_dark():
        with smtplib.SMTP("smtp.ethereal.email",587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            try:
                connection.sendmail(
                    from_addr= my_email,
                    to_addrs= my_email,
                    msg = "Subject: ISS is Nearby\n\nLOOK UP!"
                )
            except smtplib.SMTPException as e:
                print("Mail could not be delivered." ,e)
            else:
                print("Mail Sent!")
    else:
        print("You can't see ISS right now.")
    time.sleep(60)
