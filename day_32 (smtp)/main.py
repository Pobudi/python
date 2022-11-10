'''
import smtplib

my_email = "testkowal123@gmail.com"
my_password = "Haslo123."

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="kowaltest@yahoo.com", msg="Subject:Hello\n\nContent ")
'''
import datetime as dt

now = dt.datetime.now()
print(now.year)
