# Script para consultar los pagos de facturas en alegra
import requests

url = "https://api.alegra.com/api/v1/payments"

headers = {
    "accept": "application/json",
    "authorization": "Basic aW5mb0BycnNvbHVjaW9uZXNpdC5jb206ZjFhZmRlYWFmMDNiZWYwOWVjODM="
}

response = requests.get(url, headers=headers)

print(response.text)