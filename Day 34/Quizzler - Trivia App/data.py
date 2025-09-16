import requests

#  "category" : 32 ,
#     "difficult" :"easy",

PARAM = {
    "amount": 10,
    "type" : "boolean"
}

response = requests.get(url ="https://opentdb.com/api.php", params=PARAM)
response.raise_for_status()

data = response.json()

question_data = data["results"]