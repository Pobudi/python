import requests
from datetime import datetime
from os import environ
import pprint

APP_ID = environ.get("APP_ID")
API_KEY = environ.get("API_KEY")

exercise_par = {
    "query": input("What exercises have you done? "),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 185,
    "age": 19
}
my_headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
exercise_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_par, headers=my_headers)
exercise_response.raise_for_status()
result = exercise_response.json()["exercises"]

now_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%H:%M:%S")

header = {"Authorization": "Bearer L*nA6QmCd7!xg+jS"}
for exercise in result:
    docs_par = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    docs_response = requests.post(url="https://api.sheety.co/d54ac267073f4a4a6cadef09bafe07b5/cwiczenia/workouts", json=docs_par, headers=header)
    docs_response.raise_for_status()
    print(docs_response.text)

