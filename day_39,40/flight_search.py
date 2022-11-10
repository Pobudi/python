import requests
from datetime import datetime, timedelta
from pprint import pprint
from flight_data import FlightData

tequila_apikey = "sVO7zG4Qd9FtKSDNS6vb3lb9TA7w70Pj"


class FlightSearch:

    def __init__(self):
        self.indexes_to_update = []

    def check_codes(self, data):
        for city in data:
            if city["iataCode"] == "":
                print(city)
                self.indexes_to_update.append(city["id"] - 2)
                headers = {"apikey": tequila_apikey}
                parameters = {
                    "term": city["city"],
                    "location_types": "city"
                }
                tequila_response = requests.get(url="https://tequila-api.kiwi.com/locations/query", params=parameters, headers=headers)
                tequila_response.raise_for_status()
                city_data = tequila_response.json()
                city["iataCode"] = city_data["locations"][0]["code"]

    def search_flights(self, city):
        headers = {"apikey": tequila_apikey}
        tomorrow = datetime.now() + timedelta(days=1)
        six_months_now = datetime.now() + timedelta(days=6*30)

        parameters = {
            "fly_from": "WAW",
            "fly_to": city["iataCode"],
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months_now.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "PLN",
            "max_stopovers": city['stopovers'],
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
        }
        search_response = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=parameters, headers=headers)
        search_response.raise_for_status()

        try:
            data = search_response.json()["data"][0]
        except IndexError:
            print(f"\nNo flights found to {city['city']}\n")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][0]["local_departure"].split("T")[0],
                stopovers=int(len(data["route"])/2-1),
                link=data['deep_link']
            )
            return flight_data


