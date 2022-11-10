import requests
from pprint import pprint

URL = "https://api.sheety.co/d54ac267073f4a4a6cadef09bafe07b5/flightDeals/prices"

# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.headers = {"Authorization": "Bearer 8Hm(bNY1$FU9V"}
        response = requests.get(url=URL, headers=self.headers)
        response.raise_for_status()
        self.data = response.json()["prices"]

    def update_iata(self, data, indexes):
        for index in indexes:
            parameters = {
                "price": {
                    "iataCode": data[index]["iataCode"]
                }
            }
            response = requests.put(url=f"{URL}/{data[index]['id']}", headers=self.headers, json=parameters)
            response.raise_for_status()
            print(f"iata docs update: {response.text}")


