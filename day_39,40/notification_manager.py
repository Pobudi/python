#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import requests
import smtplib

my_email = "testkowal123@gmail.com"
my_password = "Haslo123."

account_sid = "ACe47824692a784dc0c668b27ad3478f8e"
auth_token = "3a3672d25b561384fc3654f5e5302c7a"


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, flight):
        text_sms = f"Tani lot! Za {flight.price} PLN z {flight.origin_city}-{flight.origin_airport}({flight.out_date}) do {flight.destination_city}-{flight.destination_airport}({flight.return_date}) z {flight.stopovers} przesiadkami "
        message = self.client.messages.create(
            body=text_sms,
            from_="+18647347031",
            to="+48692530966"
        )
        print(message.status)

    def send_emails(self, flight):
        response = requests.get(url="https://api.sheety.co/d54ac267073f4a4a6cadef09bafe07b5/flightDeals/users")
        response.raise_for_status()
        users = response.json()["users"]
        for user in users:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                text_mail = f"Subject: Dobra okazja\n\nTani lot! Za {flight.price} PLN z {flight.origin_city}-{flight.origin_airport}({flight.out_date}) do {flight.destination_city}-{flight.destination_airport}({flight.return_date}) link: {flight.link} "
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=user["email"], msg=text_mail.encode("UTF-8"))



