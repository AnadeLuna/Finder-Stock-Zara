import requests
import pandas as pd


def get_id_stores(lat,lng):
    """
    Definition : Funtion that get a list of id stores.
    
    Input: latitude,longitude
    example: 41.65500470094807, -0.8888039716475229
    
    Output: list of id stores
    example: [65, 141, 1224, 9717]
    """
    
    loc = {
    "lat":{lat},
    "lng":{lng}}   
    
    stores = "https://www.zara.com/es/es/stores-locator/search"
    
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    
    stores_id = requests.get(stores, params=loc, headers=headers).json()
    
    lst_id_stores = []
    for store in stores_id:
        lst_id_stores.append(store["id"])
        
    return lst_id_stores


def search_stores(lat,lng):
    
    """
    Definition: Funtion that get a list of id_store,latitud,longitude,address,days and schedule
    
    Input: latitude,longitude
    example: 40.416050951604056, -3.7072654155715603
    
    Output: list of dictionaries with id,latitud,longitud,adrees and day:[opening time and closing time]
    example: [{'id': 92,'latitude': 40.415669,'longitude': -3.703315,'address': 'CALLE CARRETAS, 6',
              'days': [{'L': ['10:00', '22:00'],
               'M': ['10:00', '22:00'],
               'X': ['10:00', '22:00'],
               'J': ['10:00', '22:00'],
               'V': ['10:00', '22:00'],
               'S': ['10:00', '22:00'],
               'D': ['11:00', '21:30']}}]
    """
    
    loc = {
    "lat":{lat},
    "lng":{lng}}   
    
    stores = "https://www.zara.com/es/es/stores-locator/search"
    
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    
    stores_id = requests.get(stores, params=loc, headers=headers).json()

    lsts_store= []

    for i in range(0,len(stores_id)):
    
        id_ = stores_id[i]["id"]
        latitud = stores_id[i]["latitude"]
        longitude = stores_id[i]["longitude"]
        address = stores_id[i]["addressLines"][0]
        days = stores_id[i]["openingHours"]

        week_days_dic = {1:"L", 2:"M", 3:"X", 4:"J", 5:"V", 6:"S", 7:"D"}
        day_hour = {}

        for d in days:
            try:
                day = week_days_dic[d["weekDay"]]
                open_ = d["openingHoursInterval"][0]["openTime"]
                close = d["openingHoursInterval"][0]["closeTime"]

                day_hour[day]=[open_,close]

            except:
                pass

        dir_store = {"id": id_,"latitude":latitud ,"longitude": longitude, "address":address, "days": day_hour}
        lsts_store.append(dir_store)

    return lsts_store
