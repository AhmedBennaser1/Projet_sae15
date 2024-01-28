from data_collection2 import *
from organize import *


def save_data_cars(filename,url):
    x=getting_json_data_cars(url)
    x=organize_cars(x)
    with open(f"./data_cars/{filename}.json","w") as file:
        json.dump(x,file,indent=4)
    with open(f"./data_cars/{filename}.json") as file:
        data=json.load(file) 
    return data
   


def save_data_bikes(filename,url):
    x=getting_json_data_bikes(url)
    x=organize_bikes(x)
    with open(f"./data_bikes/{filename}.json","w") as file:
        json.dump(x,file,indent=4)
    with open(f"./data_bikes/{filename}.json") as file:
        data=json.load(file) 
    return data
   
