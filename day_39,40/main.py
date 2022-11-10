#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.data


flight_search = FlightSearch()
message = NotificationManager()

flight_search.check_codes(sheet_data)
data_manager.update_iata(sheet_data, flight_search.indexes_to_update)

for city in sheet_data:
    flight = flight_search.search_flights(city)
    if flight is not None:
        if flight.price < city["lowestPrice"]:
            message.send_message(flight)
            message.send_emails(flight)



