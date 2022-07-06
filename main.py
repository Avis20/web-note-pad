
from os import sys

sys

response = os.execlp("curl dsadsa ddsa ds ads ads ad sadsa ")

response.dsadsadsa


"""
# pip install requests
import requests
import json

url = "https://api.openweathermap.org/data/2.5/weather?appid=8565a87c82886e0282fc0a1167eb3eae&lat=55.892357&lon=37.576324&units=metric"


response = requests.get(url)
response_bytes = response.content
print("response_bytes", type(response_bytes))
json_content = json.loads(response_bytes)
print("json_content", type(json_content))

main = json_content.get("main1111111111111", {"temp": "error!!!"})
print(main.get("temp"))
"""