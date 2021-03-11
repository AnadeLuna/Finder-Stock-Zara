
import requests
from src.stores import *
from src.products import *
from src.driver import driver

def get_stock(search_terms,lat,lng,driver=driver):
        """
        Definition: Function that get the stocks,url,image, product name, price, ids of products and stock of diferent sizes.
        
        Input: "search_terms",latitude,longitude,driver
        example: "cazadora amarilla",40.416050951604056, -3.7072654155715603, driver
        
        Output: list of a dictionary with url, image, product name, price, ids products and stocks.
        
        """

        products = get_products(search_terms)
  
        store_info = search_stores(lat, lng)
        store_ids = [element["id"] for element in store_info]

        stock_url = "https://itxrest.inditex.com/LOMOServiciosRESTCommerce-ws/common/1/stock/campaign/V2021/product/part-number/{}"
        stock_params = {"physicalStoreId": store_ids}

        urls = [stock_url.format("".join(p["ids_prod"]).rjust(11,"0")) for p in products]
        
        for i,product in enumerate(products):
            headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
            products[i]["stock"] = requests.get(urls[i],params=stock_params,headers=headers).json()
            
        return products