from data_collection2 import *
url="https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000" 
url2="https://portail-api-data.montpellier3m.fr/bikestation?limit=1000"
x=getting_json_data_cars(url)
y=getting_json_data_bikes(url2)
def filename_cars():
    for i in x:
        return i["availableSpotNumber"]["metadata"]["timestamp"]["value"].replace(":",".")
def filename_bikes():    
    for j in x: 
        return j["availableBikeNumber"]["metadata"]["timestamp"]["value"].replace(":",".")

