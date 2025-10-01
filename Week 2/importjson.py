# This program imports a JSON file

# Author: Loic Bagnoud

import requests
import json

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# This makes it into a readable format
with open("data", "w") as outfile:
    json.dump(data, outfile, indent=4)


print(data["northern-ireland"]["events"][0])
print(data["northern-ireland"]["events"][1])