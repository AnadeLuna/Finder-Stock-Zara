# Proyecto-Final
![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Final Project of Data Analytics Bootcamp

## Table of Content

**[Overview](#overview)**

**[Project:](#project:)**

* [Tools:](#Tools:)
* [Step 1](#step-1)
* [Step 2](#step-2)
* [Step 3](#step-3)
* [Step 4](#step-4)

**[Folder_Structure](#Folder_Structure)**

---
## Overview

The goal of this project is to demonstrate the skills I have built throughout this program of [Ironchack](https://www.ironhack.com/es). In this project, I used Python, Selenium, and Streamlit to put together a analytics workflow, including:

* Data acquisition
* Data wrangling
* Data exploration 
* Presentation 

## Project

My project is based on improving the consumer experience in the retail world.

To offer the customer the possibility of finding any product as close to him as possible and in the shortest possible time.

For all of this I have based myself on the Zara website and I am going to explain the steps I have followed and the structure of my code:

### Tools: 
####  - [Selenium](https://selenium-python.readthedocs.io/)
####  - [Requests](https://requests.readthedocs.io/en/master/)
####  - [Python](https://www.python.org/)
####  - [Pandas](https://pandas.pydata.org/)
####  - [Folium](https://python-visualization.github.io/folium/)
####  - [Streamlit](https://streamlit.io/)
####  - [Geocoder](https://geocoder.readthedocs.io/)


### Step 1

I define three functions that screen all the product information that I will need both to obtain the stock and to visualise it in the application.
I do all this by scraping the web. 

- #### Functions: 
  - get_features_products() --> Function that get the features (urlimage, product_name and price) of finded product or products and return the features.

  - get_prod_id() --> Function that get the ids (id_prod, id_color) of a product.

  - get_products() --> Function that get a list with url, image, product name and price of products. That function use function: get_features_products() and get_prod_id().
 

### Step 2

Make queries to a Zara's api to get the stores information.

- #### Functions: 
  - get_id_stores() --> Function that get a list of id stores.

  - search_stores() --> Function that get a list of id_store,latitud,longitude,address,days and schedule


### Step 3

This is the most important part and where the most relevant information is kept. For this, we are going to need the product ids and the shop id that we have previously extracted.

- #### Function: 
  - get_stock() --> Function that get the stocks,url,image, product name, price, ids of products and stock of diferent sizes.


### Step 4

To demonstrate my project, I used Selium, which helped me a lot to convey the most important information.


### Folder_Structure

- In the `jupyter notebooks` folder you will find different files in which I test all my code before use it into the `.py` files.

- In `scr` you can find all the code with functions in `.py`. Files:
  - driver.py --> It´s a code just to connect with chromedriver.
  - products.py --> Function from `Step 1`.
  - stores.py --> Functions from `Step 2`.
  - stocks.py --> Functions from `Step 3`.
  - chromedriver

- In `demo.py` you can find all the code for the MVP (minimum viable product)





