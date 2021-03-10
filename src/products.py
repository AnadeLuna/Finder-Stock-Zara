from time import sleep
from src.driver import driver

def get_features_products(search_terms, driver=driver):
    """
    Definition : Funtion that get the features (url, image, product_name and price) 
    of finded product or products and return the features.
    
    Input: 'search_terms' , driver 
    example: 'cazadora amarilla', driver
    
    Output: list of dictionary or dictionaries.    
    example: [{"url": [] ,"image": [],"product_name": [], "price": []}
    """

    driver.get("https://www.zara.com/es/es/search")
    sleep(1)
    try:
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        sleep(1)
    except: pass
    
    search = driver.find_element_by_id("search-term")
    search.click()
    search.send_keys(search_terms)
    sleep(1)
    all_url_prod = driver.find_elements_by_css_selector("#products > ul > section > ul > li")

    lst_dic_total_prod = []

    for url in all_url_prod:

        dic_total_prod = {"url": [] ,"image": [],"product_name": [], "price": []}


        dic_total_prod["url"] = url.find_element_by_css_selector("div > div > a").get_attribute("href")

        dic_total_prod["image"] = url.find_element_by_css_selector("a > div > div > div > picture > img").get_attribute("src")

        dic_total_prod["product_name"] = url.find_element_by_css_selector("div > div > a > span").text

        dic_total_prod["price"] = url.find_element_by_css_selector("div > div > div.product-grid-product-info__price.price > span").text

        lst_dic_total_prod.append(dic_total_prod)

    return lst_dic_total_prod
    



def get_prod_id(product_url, driver=driver):
    
    """
    Definition: Funtion that get the ids (id_prod, id_color) of a product.
    
    Input: 'search_terms' , driver 
    example: 'cazadora amarilla', driver
    
    Output: [id_prod, id_color]
    example: ['3427741', '320']
    """
    
    driver.get(product_url)
    sleep(1)
    try: 
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        sleep(1)
        
    except: pass
    driver.find_element_by_class_name("product-detail-actions__action-button").click()
    sleep(1)
    ids_prod = driver.find_element_by_css_selector("#theme-modal-container > div > div > div > div > div.modal__body.modal__body--spacer-bottom > p")

    ids_prod = ids_prod.find_elements_by_css_selector("p")[:2]
    ids_prod = [element.text.split("_")[-1] for element in ids_prod ]

    lst_ids_prod = ["".join([caracter for caracter in element if caracter.isnumeric()]) for element in ids_prod]

    return lst_ids_prod



def get_products(search_terms,driver=driver):
    
    """
    Definition: Funtion that get a list with url, image, product name and price of products.
    That function use function: get_features_products() and get_prod_id().
    
    Input: 'search_terms' , driver 
    example: 'cazadora amarilla', driver
    
    Output: list of a dictionary with url, image, product name, price, ids of products.
    example: [{'url': 'https://www.zara.com/es/es/blusa-crop-tie-dye-p00085048.html',
              'image': 'https://static.zara.net/photos///2021/V/0/1/p/0085/048/947/2/w/200/0085048947_1_1_1.jpg?ts=1615206456459',
              'product_name': 'BLUSA CROP TIE DYE',
              'price': '25,95 EUR',
              'ids_prod': ['0085048', '947']}]
    """
    
    products = get_features_products(search_terms)
    for i,product in enumerate(products):
        
        product_url = product["url"]
        
        url_ids = get_prod_id(product_url)
     
        products[i]["ids_prod"] = url_ids
    
    return products