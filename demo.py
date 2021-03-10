import streamlit as st
from PIL import Image
import geocoder
from src.stocks import *
from src.driver import driver
import folium
from streamlit_folium import folium_static



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

    #Information
    #prod_stock = None
    #prod_stock = get_stock(search_terms,lat,lng)


#Ejemplos de como 
    #Imagen 
    #img = 'https://static.zara.net/photos///2021/V/0/1/p/0085/048/947/2/w/200/0085048947_1_1_1.jpg?ts=1615206456459'
    #st.image(img, width=300)
    
    #Producname and price
    #st.subheader("Nombre Product")
    #st.subheader("Precio")

    #map
    #map_1 = folium.Map(location = [lat,lng], zoom_start = 12)
    #folium_static(map_1)
    #explicado en el jupyter

    #Talla y stock 
    #dateframe
    #size = st.selectbox("")

    





    #st.write("codenadas:",cordenadas)
    #st.write(prod_stock)
