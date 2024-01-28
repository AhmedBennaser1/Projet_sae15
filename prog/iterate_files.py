import os 
from les_places_disponibles import *
avg_cars=open("avg_cars.txt","w")
avg_bikes=open("avg_bikes.txt","w")
f2=open("occup-cars.txt","w",encoding='UTF-8')
f3=open("occup-bikes.txt","w",encoding='UTF-8')
x=0
def path_c(f2,x):
    path="./data_cars/"
    directory = os.fsencode(path)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        path=f'./data_cars/{filename}'
        time=path[1:].find(".")
        temps=path[time-1:time+4].replace('.','h')
    

        occup_c(path,f2,temps)
        moyen_c(path,avg_cars,temps)
        x+=30
path_c(f2,x)

def path_b(f3,x):
    path="./data_bikes/"
    directory = os.fsencode(path)
  
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        path=f'./data_bikes/{filename}'
        time=path[1:].find(".")
        temps=path[time-1:time+4].replace('.','h')   


        occup_b(path,f3,temps)
        moyen_b(path,avg_bikes,temps)
        x+=30
path_b(f3,x)
#https://fr.wikihow.com/calculer-un-%C3%A9cart-type calculer l'écart type