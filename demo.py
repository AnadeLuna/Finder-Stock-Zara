import streamlit as st
from PIL import Image
import geocoder
from src.stocks import *
from src.stores import *
from src.driver import driver
import folium
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map
import pandas


imagen = Image.open("images/Portada.png")
st.image(imagen)

st.header("¿Qué estás buscando?")
search_terms = st.text_input("Buscador:")


st.header("¿Dónde te encuentras?")
location = st.text_input("Localización:")

if st.button("Aceptar"):

    #Transform to a cordenates
    st.write("Buscando resultados")
    loc = geocoder.osm(location)
    cordenadas = loc.latlng
    lat = cordenadas[0]
    lng = cordenadas[1]


    # Map
    locat = search_stores(lat,lng)
    df2 = pd.DataFrame(locat)
    

    map_1 = folium.Map(location = [lat,lng], zoom_start = 12)

    icono = Icon(color = "blue",
             prefix = "fa",
             icon = "fa-map-marker",
             icon_color = "white",)

    loc = {"location":[lat,lng],
        "tooltip": "Mi ubicación"}
   
    marker_ = Marker(**loc, icon = icono).add_to(map_1)


    for i,row in df2.iterrows():
        
        location_ = {"location" : [row["latitude"],row["longitude"]], "tooltip" : row["id"]}
        
        icon = Icon(color = "yellow",
                    prefix = "fa",
                    icon = "shopping-bag",
                    icon_color = "black")

        Marker(**location_,icon=icon,popup=row["address"]).add_to(map_1)

    folium_static(map_1)
    

    
    #Information product
    prod_stock = get_stock(search_terms,lat,lng)

    for product in prod_stock:

        #Image
        img= product["image"]
        st.image(img, width=300)

        #Product Name
        st.write(product["product_name"])
        
        #Product Price
        st.write(product["price"])

        #Stock
        for stock in product["stock"]["stocks"]:
            
            size_stk = []

            for sizeStock in stock["sizeStocks"]:

                size_stock = {}

                #Product size
                size_ = {101:"XS", 102:"S", 103:"M", 104:"L", 105:"XL", 106:"XXL",125:"S-M",131:"L-XL"}
                if sizeStock["size"] in size_:
                    sizeStock["size"] = size_[sizeStock["size"]]
                
                    size_stock["Talla"] = sizeStock["size"]
                else:
                    size_stock["Talla"] = sizeStock["size"]

                #Normalize quantity:
                if sizeStock["quantity"] <= 0:
                    size_stock["Stock"] = "Sin existencias"
                elif sizeStock["quantity"] == 1:
                    size_stock["Stock"] = "Pocas existencias"
                    
                elif sizeStock["quantity"] >= 2:
                    size_stock["Stock"] = "Existencias"
                    
                elif sizeStock["quantity"] >= 4:
                    size_stock["Stock"] = "Muchas existencias"


                #Check if there is stock
                if size_stock["Stock"] == "Sin existencias":
                    pass
                else: 
                    size_stk.append(size_stock)
            

            if len(size_stk) > 0:
                st.write("id tienda:",stock["physicalStoreId"])
                df1 = pd.DataFrame(size_stk)
                st.write(df1)
   
   
   
   


                

