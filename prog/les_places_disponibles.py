import json
def occup(data, f, diff):
    import json

#pour parl-king voiture 

def dispo_c(data_c):
    som=0
    l=[]
    for i in data_c:
        if i["status"]=="Open": 
            x=(i["name"],i["availableSpotNumber"])
            l.append(x) 
    for j in l:
        print("Les places disponibles dans ",j[0],"est",round(j[1],2)) 
        som+=j[1]
    print()
    print("le total des places disponibles dans montpellier est ",som)
    print()  

def moyen_c(path_c,f1,temp):
    with open(path_c) as f:
        data=json.load(f)
        print(data)

    
    l=[]
    for i in data:
        sparking = i["name"]
        if i["status"]=="Open":
            l.append(((i["totalSpotNumber"]-i["availableSpotNumber"])/i['totalSpotNumber'])*100)
    
        f1.write(f"{sparking}:"+str(round(sum(l)/len(l),2))+":"+temp+"\n")
    
    print(f"{sparking}:",round(sum(l)/len(l),2),"%")
    print()
        

def occup_c(path_c,f2,temp):
    with open(path_c) as f:
        data=json.load(f)
        print(data)

    l1=[]
    for i in data:
        sparking = i["name"]
        occup =round(((i["totalSpotNumber"] - i["availableSpotNumber"]) / i["totalSpotNumber"])*100,2)
        l1.append(occup)
        print(i, occup)
        f2.write(sparking+":"+str(occup)+":"+temp+"\n")
    print()
    print("the total occup est", round(sum(l1)/len(l1),2))
    print()
    
      



#pour parking velo 
def dispo_b(data_b):
    som=0
    l=[]
    for i in data_b:
        if i["status"]=="working": 
            x=(i["address"],i["availableBikeNumber"])
            l.append(x) 
    for j in l:
        print("Les velos disponibles dans ",j[0],"est",round(j[1],2)) 
        som+=j[1]
    print()
    print("les velos disponibles dans montpellier total est ",som)
    print()  


def moyen_b(path_b,f2,temp):
    with open(path_b) as f:
        data=json.load(f)
        print(data)

    l=[]
    for i in data:
        sparking=i['address']
        if i["status"]=="working":
            l.append(((i["totalSlotNumber"]-i["availableBikeNumber"])/i["totalSlotNumber"])*100)
        
        f2.write(f"{sparking}:"+str(round(sum(l)/len(l),2))+":"+temp+"\n")
    print("remplissage moyen  pour parking velo est :",round(sum(l)/len(l),2),"%")
    print()
    


def occup_b(path_b,f3,temp):
    with open(path_b) as f:
        data=json.load(f)
    print(data)
    l1=[]
    for i in data:
        sparking = i["address"]
        occup =round(((i["totalSlotNumber"] - i["availableBikeNumber"]) / i["totalSlotNumber"])*100,2)
        l1.append(occup)
        print(i, occup)
        f3.write(sparking+":"+str(occup)+":"+temp+"\n")
    print("the total occup pour velo est", round(sum(l1)/len(l1),2),"%")


  

