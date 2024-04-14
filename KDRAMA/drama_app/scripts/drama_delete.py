import requests
id = 9

api_url = f'http://localhost:8000/drama/drama_app/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print('Drama Deleted Successfully')
else:
    print('Error deleting Drama')