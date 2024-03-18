API_URL = "http:127.0.0.1:8000"

import requests

response = requests.get(f'{API_URL}/api/classroom-viewset/1/')

print(response.text)
