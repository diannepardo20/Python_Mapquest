import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "1fRfZdxZ6MksxGxYZ8k81IeaR9ASo5pI"


while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
