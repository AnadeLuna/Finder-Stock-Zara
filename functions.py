
from selenium import webdriver
from time import sleep
import requests

driver = webdriver.Chrome("./chromedriver")

## list_ids_products

def search_products(search_terms, driver):

    driver.get("https://www.zara.com/es/es/search")
    sleep(1)
    try:
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        sleep(1)
        search = driver.find_element_by_id("search-term")
        search.click()
        search.send_keys(search_terms)
        sleep(1)
        all_url_prod = driver.find_elements_by_css_selector("#products > ul > section > ul > li")

        lst_urls = []
        for url in all_url_prod:
            lst_urls.append(url.find_element_by_css_selector("div > div > a").get_attribute("href"))

        return lst_urls
    except:
        sleep(1)
        search = driver.find_element_by_id("search-term")
        search.click()
        search.send_keys(search_terms)
        sleep(1)
        all_url_prod = driver.find_elements_by_css_selector("#products > ul > section > ul > li")

        lst_urls = []
        for url in all_url_prod:
            lst_urls.append(url.find_element_by_css_selector("div > div > a").get_attribute("href"))

        return lst_urls
    



    def get_prod_id(prod_url, driver):
    
        driver.get(prod_url)
        sleep(1)
        try: 
            driver.find_element_by_id("onetrust-accept-btn-handler").click()
            sleep(1)
            driver.find_element_by_class_name("product-detail-actions__action-button").click()
            sleep(1)
            ids_prod = driver.find_element_by_css_selector("#theme-modal-container > div > div > div > div > div.modal__body.modal__body--spacer-bottom > p")

            ids_prod = ids_prod.find_elements_by_css_selector("p")[:2]
            ids_prod = [element.text.split("_")[-1] for element in ids_prod ]
            
            lst_ids_prod = ["".join([caracter for caracter in element if caracter.isnumeric()]) for element in ids_prod]

            return lst_ids_prod
        except:
            
            driver.find_element_by_class_name("product-detail-actions__action-button").click()
            sleep(1)
            ids_prod = driver.find_element_by_css_selector("#theme-modal-container > div > div > div > div > div.modal__body.modal__body--spacer-bottom > p")

            ids_prod = ids_prod.find_elements_by_css_selector("p")[:2]
            ids_prod = [element.text.split("_")[-1] for element in ids_prod ]
            
            lst_ids_prod = ["".join([caracter for caracter in element if caracter.isnumeric()]) for element in ids_prod]

            return lst_ids_prod
    



    def get_products(search_terms,driver):
    
        lst_ids = []
        for prod_url in search_products(search_terms, driver):
            #print(prod_url)
            url_ids = get_prod_id(prod_url, driver)
            #print(url_ids)
            lst_ids.append(url_ids)   
        return lst_ids

    
## list_stores

    def search_stores(lat,lng):
    
        loc = {
        "lat":{lat},
        "lng":{lng}}   
        
        stores = "https://www.zara.com/es/es/stores-locator/search"
        
        stores_id = requests.get(stores, params=loc).json()
        
        lst_id_stores = []
        for store in stores_id:
            lst_id_stores.append(store["id"])

            
        return lst_id_stores
            


    def search_stores(lat,lng):
    
        loc = {
        "lat":{lat},
        "lng":{lng}}   
        
        stores = "https://www.zara.com/es/es/stores-locator/search"
        
        stores_id = requests.get(stores, params=loc).json()

        lsts_store= []

        for i in range(0,len(stores_id)):

            id_ = store_id[i]["id"]
            latitud = store_id[i]["latitude"]
            longitude = store_id[i]["longitude"]
            adress = store_id[i]["addressLines"][0]
            days = store_id[i]["openingHours"]

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

            dir_store = {"id": id_,"latitude":latitud ,"longitude": longitude, "adress":adress, "days": day_hour}
            lsts_store.append(dir_store)

        return lsts_store