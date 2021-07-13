import requests
import os
from datetime import datetime, date

NUTRITION_APP_ID = os.environ.get("NUTRITION_APP_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")

nutrition_url = os.environ.get("NUTRITION_URL")
sheety_url = os.environ.get("SHEETY_URL")


json_param = {
    "query": input("What exercise did you do today? "),
    "gender": "male",
    "weight_kg": 77.7,
    "height_cm": 177.67,
    "age": 33
}

headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY
}

response = requests.post(url=nutrition_url, json=json_param, headers=headers)
print(response.json())
stat_json = response.json()['exercises']
date_formatted = date.today().strftime("%d/%m/%Y")
time_formatted = datetime.now().strftime("%H:%M:%S")

for exc in stat_json:
    sheety_add_param = {
        "workout":
            {
                "date":date_formatted,
                "time":time_formatted,
                "exercise":exc['name'].title(),
                "duration":exc['duration_min'],
                "calories":exc['nf_calories']
            }
    }

    response = requests.post(url=sheety_url,json=sheety_add_param)
    print(response.text)
print("Project completed successfully done")

