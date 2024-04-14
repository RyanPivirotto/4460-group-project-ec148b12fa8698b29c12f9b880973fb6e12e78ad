import requests
import json

id = 8

api_url = f'http://localhost:8000/drama/drama_app/{id}/'

drama_data = {
   "title" : "Drama 2",
    "start_date":"2022",
    "director" : "Bot Smith",
    "seasons" : "2",
    "characters" : "13",
    "actors" : "13",
}

response = requests.put(api_url, data=json.dumps(drama_data), headers={'Content-Type': 'application/json'})

if response.status_code==200:
    print('Drama Updated Successfully')
else:
    print('error updating Drama')