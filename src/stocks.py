from selenium import webdriver
import requests
from src.stores import *
from src.products import *


def get_stock(search_terms,lat,lng):
        """
        Definition: Funtion that get the stocks,url,image, product name, price, ids of products and stock of diferent sizes.
        
        Input: "search_terms",latitude,longitude
        example: "cazadora amarilla",40.416050951604056, -3.7072654155715603
        
        Output: list of a dictionary with url, image, product name, price, ids products and stocks.
        example:[{'url': 'https://www.zara.com/es/es/blusa-crop-tie-dye-p00085048.html',
                  'image': 'https://static.zara.net/photos///2021/V/0/1/p/0085/048/947/2/w/200/0085048947_1_1_1.jpg?ts=1615206456459',
                  'product_name': 'BLUSA CROP TIE DYE',
                  'price': '25,95 EUR',
                  'ids_prod': ['0085048', '947']
                    'stock': .......}]

        """
    
        driver = webdriver.Chrome("./chromedriver")

        products = get_products(search_terms,driver)

        driver.close()

        store_info = search_stores(lat, lng)
        store_ids = [element["id"] for element in store_info]

        stock_url = "https://itxrest.inditex.com/LOMOServiciosRESTCommerce-ws/common/1/stock/campaign/V2021/product/part-number/{}"
        stock_params = {"physicalStoreId": store_ids}

        urls = [stock_url.format("".join(p["ids_prod"]).rjust(11,"0")) for p in products]
        
        for i,product in enumerate(products):
            products[i]["stock"] = requests.get(urls[i],params=stock_params).json()
            
        return products