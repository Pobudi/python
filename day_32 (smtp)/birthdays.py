import datetime as dt
import pandas
import smtplib
from random import randint

my_email = "testkowal123@gmail.com"
my_password = "Haslo123."

month = dt.datetime.now().month
day = dt.datetime.now().day

birthdays_data = pandas.read_csv("birthdays.csv")
birthday_people = birthdays_data[(birthdays_data.day == day) & (birthdays_data.month == month)].to_dict(orient="records")

for person in birthday_people:
    with open(f"./letter_templates/letter_{randint(1,3)}.txt") as temp_letter:
        text = temp_letter.read()
        message = "Subject:Happy birthday!\n\n" + text.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=message)



