
from selenium import webdriver
import os
options = webdriver.ChromeOptions()
options.add_argument("headless")
#driver = webdriver.Chrome(executable_path="../chromedriver", chrome_options = options)
path = os.path.join(os.getcwd(), "chromedriver")
driver = webdriver.Chrome(executable_path=path, chrome_options = options)


