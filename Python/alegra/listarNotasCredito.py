# Script para consultar la informacionnotas credito generadas en alegra
import requests

url = "https://api.alegra.com/api/v1/credit-notes"

headers = {
    "accept": "application/json",
    "authorization": "Basic aW5mb0BycnNvbHVjaW9uZXNpdC5jb206ZjFhZmRlYWFmMDNiZWYwOWVjODM="
}

response = requests.get(url, headers=headers)

print(response.text)