from dotenv import load_dotenv
import requests
import os
from datetime import datetime

load_dotenv()

# Personal Data
gender = "female"
weight_kg = 46
height_cm = 160
age = 21

# Environment Variables
APP_ID= os.getenv("NUTRI_API_ID")
APP_KEY = os.getenv("NUTRI_API_KEY")
nutri_endpoint = os.getenv("nutri_endpoint")
sheety_endpoint = os.getenv("sheety_endpoint")
SHEET_AUTH = os.getenv("SHEETY_AUTH")

# User input
query = input("Tell me what exercise you performed: ")

# define parameters and headers for accessing  Nutritionix API
parameters = {
    "query" : query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY
}

# post the query to api
response = requests.post(url = nutri_endpoint, headers= header, json= parameters)
response.raise_for_status()
nutri_output = response.json()

# for current date and time
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

# define parameters and headers for accessing  Sheety API
headers ={
    "Authorization" : SHEET_AUTH
}

workout_entry = {}

for exercise in nutri_output["exercises"]:
    workout_entry = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # post the data to google sheet
    post_response = requests.post(url=sheety_endpoint, json=workout_entry, headers= headers)
    print(post_response.text)
