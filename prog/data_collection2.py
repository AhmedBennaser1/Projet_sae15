import requests
import json

def getting_json_data_cars(url):
    response=requests.get(url) 
    data=response.json() 
    with open("parkingvoiture.json","w") as file:
        json.dump(data,file,indent=4)
    return data    
    

def getting_json_data_bikes(url):
    response=requests.get(url) 
    data=response.json()
    with open("parkingvelo.json","w") as file:
        json.dump(data,file,indent=4) 
    return data    
        
        