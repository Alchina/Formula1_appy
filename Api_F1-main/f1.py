import requests


url_drivers = "https://f1-live-motorsport-data.p.rapidapi.com/drivers/standings/2023"
url_constructor = "https://f1-live-motorsport-data.p.rapidapi.com/constructors/standings/2023"
url_races = "https://f1-live-motorsport-data.p.rapidapi.com/races/2023" 

headers = {
	"X-RapidAPI-Key": "1f34dca956msh225f5bcc3536bf2p1aac41jsn9c1db12ddb55", 
	"X-RapidAPI-Host": "f1-live-motorsport-data.p.rapidapi.com"
}

response_drivers = requests.get(url_drivers, headers=headers) 
response_constructor = requests.get(url_constructor, headers=headers)
response_races = requests.get(url_races, headers=headers)