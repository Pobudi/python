import smtplib
import random
import datetime as dt

with open("./quotes.txt",  "r") as quotes:
    list_quotes = quotes.readlines()

now = dt.datetime.now().weekday()
if now == 1:
    message = "Subject:Motivational mail\n\n" + random.choice(list_quotes)

    my_email = "testkowal123@gmail.com"
    my_password = "Haslo123."

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="kowaltest@yahoo.com", msg=message)




