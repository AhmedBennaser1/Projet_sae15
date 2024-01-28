import folium
from folium import IFrame
from data_collection2  import *
from organize import *
from les_places_disponibles import *
import json

url_cars = "https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000" 
url_bikes = "https://portail-api-data.montpellier3m.fr/bikestation?limit=1000"

map = folium.Map(location=[43.61, 3.87], zoom_start=12.5)

points = []

pc = getting_json_data_cars(url_cars)
pb = getting_json_data_cars(url_bikes)
x_c=[]
x_b=[]
for i in pc: 
    placesdispo = i["availableSpotNumber"]["value"]
    placestotal = i["totalSpotNumber"]["value"]
    taux = round(((placestotal - placesdispo) / placestotal) * 100, 2)
    x_c.append(taux)
    l = i["location"]["value"]["coordinates"]
    label = (f"parking voiture : {i['name']['value']}<br>"
             f"places dispo : {placesdispo}<br>"
             f"places totales : {placestotal}<br>"
             f"le taux d'occupation : {taux}%")
    l.append(label)
    if taux > 80:
        l.append("red")
    elif 40 <= taux <= 80:
        l.append('orange')
    else:
        l.append("green")
        
    l.append('car')
    points.append(l)

    
    

for i in pb:
    placestotal = i["totalSlotNumber"]["value"]
    velodispo = i["availableBikeNumber"]["value"]
    placesdispo = placestotal - velodispo
    taux = round(((placestotal - placesdispo) / placestotal) * 100, 2)
    x_b.append(taux)
    l = i["location"]["value"]["coordinates"]
    label = (f"parking velo : {i['address']['value']['streetAddress']}<br>"
             f"places dispo : {placesdispo}<br>"
             f"places totales : {placestotal}<br>"
             f"le nombre de velo dispo : {velodispo}<br>"
             f"le taux d'occupation : {taux}%")
    l.append(label)
    if taux > 80:
        l.append("purple")
    elif 40 <= taux <= 80:
        l.append('darkblue')
    else:
        l.append("bleu")
    l.append('bike')
    points.append(l)
    
    

for lon, lat, label, color, type in points:
    icon = folium.Icon(color=color, icon='info-sign')  
    if type == 'car':
        icon = folium.Icon(color=color, icon='car', prefix='fa')  
    elif type == 'bike':
        icon = folium.Icon(color=color, icon='bicycle', prefix='fa')  

    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(label, max_width=450),
        icon=icon
    ).add_to(map)
moy_occup_c=l=sum(x_c)/len(x_c)
moy_occup_b=l=sum(x_b)/len(x_b)

print(moy_occup_b,moy_occup_c)

legend_html = '''
<div style="position: fixed; 
     bottom: 5%px; left: 1.5%px; width: 160px; height: auto; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white; padding:10px;
     @media screen and (max-width: 600px) {
    .legend {
        font-size: 10px; /* Adjust font size for smaller screens */
    }   
">
     &nbsp; Légende <br>
     &nbsp; Parking voiture &nbsp; <i class="fa fa-car" style="color:red"></i><br>
     &nbsp; Parking vélo &nbsp; <i class="fa fa-bicycle" style="color:blue"></i><br>
     &nbsp; Taux d'occupation: <br>
     &nbsp; <i class="fa fa-square" style="color:green"></i>&nbsp; < 40% (Faible) <br>
     &nbsp; <i class="fa fa-square" style="color:orange"></i>&nbsp; 40% - 80% (Moyen) <br>
     &nbsp; <i class="fa fa-square" style="color:red"></i>&nbsp; > 80% (Élevé) <br>
</div>
'''
moy_occup_c = sum(x_c) / len(x_c)
moy_occup_b = sum(x_b) / len(x_b)



map.get_root().html.add_child(folium.Element(legend_html))


map.save("map.html")


