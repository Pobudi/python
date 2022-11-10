import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": "0olkmjkl.,mjhy6543wedf",
    "username": "pobudi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/pobudi/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "hours tracking",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}
headers = {"X-USER-TOKEN": user_parameters["token"]}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/pobudi/graphs/{graph_parameters['id']}"
pixel_parameters = {
    "date": today,
    "quantity": "3"
}

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)
pixel_endpoint_put = f"{pixel_endpoint}/{today}"
update_parameters = {
    "quantity": "4",
}

response = requests.put(url=pixel_endpoint_put, json=update_parameters, headers=headers)
print(response.text)

