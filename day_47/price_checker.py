import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_gmail = "testkowal123@gmail.com"
my_password = "Haslo123."

amzn_url = "https://www.amazon.com/ASUS-Ultra-Slim-Innovative-Screenpad-UX434FL-DB77/dp/B07T1DZGKQ/ref=sr_1_6?crid" \
           "=2EEW2FPR23S3L&keywords=asus+zenbook+14+ux433f&qid=1646562525&sprefix=asus+zenbook+14+ux433f%2Caps%2C192" \
           "&sr=8-6 "
headers = {
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
}
am = requests.get(url=amzn_url, headers=headers)
soup = BeautifulSoup(am.text, "lxml")
price = float(soup.find_all(name="span", class_="a-price-whole")[0].getText().split(".")[0].replace(",", "."))

if price < 1700:
    print(amzn_url)
    msg = f"subject: AMAZON PRICE TRACKER\n\nplayka is now {price} you can get it now via\n{amzn_url}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_password)
        connection.sendmail(from_addr=my_gmail, to_addrs="103bartek@gmail.com", msg=msg)
