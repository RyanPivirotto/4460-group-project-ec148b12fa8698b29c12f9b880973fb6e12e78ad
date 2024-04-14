import requests

id=1

api_url = f'http://localhost:8000/drama/drama_app/{id}'

response = requests.get(api_url)

if response.status_code==200:
    drama_data = response.json()
    print(drama_data)
else:
    print('Error retrieving Drama')