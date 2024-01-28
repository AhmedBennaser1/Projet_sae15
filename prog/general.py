from data_collection2 import *
from saving_data import *
from les_places_disponibles import *
from filename import *
import time
import datetime
from iterate_files import *
from printing_data import *

url_cars="https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000" 
url_bikes="https://portail-api-data.montpellier3m.fr/bikestation?limit=1000"
ex_t=1800
temps=time.time() 
end=temps+ex_t 

while end-temps>=0: 
    filena=datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    getting_json_data_cars(url)
    getting_json_data_bikes(url)
    
    
    data_cars=save_data_cars(filena,url_cars) 
    dispo_c(data_cars)
    
    data_bikes=save_data_bikes(filena,url_bikes) 
    dispo_b(data_bikes)
    
    print()

    temps=time.time()
    



    
    time.sleep(10)
    x+=1

print("done") 


