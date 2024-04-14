import requests
import json

api_url = 'http://localhost:8000/drama/drama_app/'

drama_data = {
    "title" : "Drama 1",
    "start_date":"2023",
    "director" : "Bob Smith",
    "seasons" : "3",
    "characters" : "12",
    "actors" : "12",
}

response = requests.post(url= api_url, data=json.dumps(drama_data),headers={'Content-Type':'application/json'})    

if response.status_code == 201:
    print('Drama created succesfully')
else:
    print(f'Error creating Drama.')