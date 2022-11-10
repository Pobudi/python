import requests
import datetime
import time
import smtplib

MY_LAT = 52.2319581
MY_LONG = 21.0067249
MY_EMAIL = "testkowal123@gmail.com"
MY_PASSWORD = "Haslo123."

while True:
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    location = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "date": "2021-03-30",
        "formatted": 0
    }

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.datetime.now().hour

    if ((now < sunrise) or (now > sunset)) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5) and (MY_LAT - 5 < iss_latitude < MY_LAT + 5):
        print("email sent")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(to_addrs="kowaltest@yahoo.com", from_addr=MY_EMAIL, msg="Subject:ISS\n\nLook up!")
        break

    time.sleep(60)

