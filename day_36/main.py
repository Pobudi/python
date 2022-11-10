import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_key = "NLHVXB9AENJJKYVF"
news_key = "9cf5232f19624fa39619c323276c4902"

account_sid = "ACe47824692a784dc0c668b27ad3478f8e"
auth_token = "3a3672d25b561384fc3654f5e5302c7a"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_key
    }
alpha_response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
alpha_response.raise_for_status()
data = alpha_response.json()['Time Series (Daily)']

# uzyskuje daty dzisiaj, przedwczoraj i przed przed wczoraj
today = datetime.now() - timedelta(days=9)
yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")
before_yesterday = (today - timedelta(days=2)).strftime("%Y-%m-%d")

# sprawdzam czy gielda byla otwarta wczoraj i przedwczoraj
try:
    yesterday_data = data[yesterday]
    before_yesterday_data = data[before_yesterday]
except KeyError:
    print("Was closed")
else:
    percent_diff = (float(yesterday_data["4. close"]) - float(before_yesterday_data["1. close"])) / float(yesterday_data["4. close"]) * 100

    down_or_up = "🔺"
    if percent_diff >= 5 or percent_diff <= 5:
        if percent_diff < 0:
            down_or_up = "🔻"

        news_parameters = {
            "qInTitle": COMPANY_NAME,
            "apiKey": news_key,
            "sortBy": "publishedAt"
        }
        news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
        news_response.raise_for_status()
        news_data = news_response.json()["articles"]

        client = Client(account_sid, auth_token)
        for article in news_data[:3]:
            formatted_message = f"{STOCK}: {down_or_up}{abs(round(percent_diff, 2))}% \nHeadline: {article['title']}\nBrief: {article['description']}"
            message = client.messages.create(
                from_="+18647347031",
                to="+48692530966",
                body=formatted_message)

            print(message.status)
