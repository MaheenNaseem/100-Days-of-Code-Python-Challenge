import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USER= os.getenv("PIXELA_USERNAME")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

header = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

# ---------------------------- CREATING USER ----------------------------

user_parameters = {
    "token" : PIXELA_TOKEN,
    "username" :PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

user_response = requests.post(PIXELA_ENDPOINT, json =user_parameters)
print(user_response.text)


# ---------------------------- CREATING A GRAPH ----------------------------

graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"
quantity = input("Enter the pages you read: ")

graph_config = {
    "id" : "graph1",
    "name" : "Reading Graph",
    "unit" : "pages",
    "type" : "int",
    "color": "ajisai"
}

graph_response = requests.post(url = graph_endpoint, headers = header, json = graph_config)
print(graph_response.text)

# ---------------------------- POSTING A PIXEL ----------------------------

pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/graph1"
quantity = input("Enter the pages you read: ")

now = dt.datetime.now()
date = now.strftime("%Y%m%d")

pixel_parameter = {
    "date" : date,
    "quantity" : quantity
}

pixel_response = requests.post(url = pixel_endpoint, headers= header, json=pixel_parameter)
print(pixel_response.text)

# ---------------------------- UPDATING A PIXEL ----------------------------

quantity = input("Enter the pages you read: ")

update_pixel_endpoint = f"{pixel_endpoint}/20250920"
updating_pixel_parameters = {
    "quantity" : quantity
}

updating_response = requests.put(url = update_pixel_endpoint, headers= header, json = updating_pixel_parameters)
print(updating_response.text)

# ---------------------------- DELETE A PIXEL ----------------------------

delete_pixel_endpoint = f"{pixel_endpoint}/20250920"

delete_response = requests.delete(url = delete_pixel_endpoint, headers= header)
print(delete_response.text)
