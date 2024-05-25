# Script para consultar la informacion de un pago X en alegra
import requests

url = "https://api.alegra.com/api/v1/payments/id"

headers = {
    "accept": "application/json",
    "authorization": "Basic aW5mb0BycnNvbHVjaW9uZXNpdC5jb206ZjFhZmRlYWFmMDNiZWYwOWVjODM="
}

response = requests.get(url, headers=headers)

print(response.text)