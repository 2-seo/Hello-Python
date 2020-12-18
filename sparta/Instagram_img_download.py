import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import os

# Get instagram id
URL = input('Instagram URL: ')

# Set the web driver file path
driver = webdriver.Chrome('./chromedriver')
driver.get(URL)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# Get Image URL from URL
imageURL = soup.select_one('div.KL4Bh > img')['src']
dload.save(imageURL, 'img/download2.jpeg')['src']

driver.quit()