import requests

url = "http://notify2.qa.fonmix.ru/api/red/task/add"

payload = {
    "transport": "email",
    "template": "fonmix_custom_message",
    "recipient": ["vajil31327@ippals.com", "nilobek469@snowlash.com"],
}
files = []
headers = {
    "X-Secret-Key": "c987581085ec9b5a5e949a915417f8bc",
    "Cookie": "uid=W20TNmQ9CYSRETarA2e0Ag==",
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

import json
print(json.dumps(response.json(), indent=2, default=str, ensure_ascii=False))
