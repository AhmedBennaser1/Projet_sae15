

def organize_cars(data):
    s=[]
    dict={}
    for i in data:
        dict={"id": i["id"],
        "status": i["status"]["value"],
        "totalSpotNumber": i["totalSpotNumber"]["value"],
        "name": i["name"]["value"], 
        "availableSpotNumber": i["availableSpotNumber"]["value"],"localisation":i["location"]["value"]["coordinates"]}

        s.append(dict)
    return s


def organize_bikes(data):
    s=[]
    dict={}
    for i in data:
        dict={"id": i["id"],
        "status": i["status"]["value"],
        "totalSlotNumber": i["totalSlotNumber"]["value"],
        "address": i["address"]["value"]["streetAddress"], 
        "availableBikeNumber": i["availableBikeNumber"]["value"],"localisation":i["location"]["value"]["coordinates"]}

        s.append(dict)
    return s

