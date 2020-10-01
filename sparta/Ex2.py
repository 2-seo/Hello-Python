import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%9E%88%EC%A7%80+%EC%9C%A0%EB%82%98") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

thumnails = soup.select('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div > a.thumb._thumb > img')

i = 1
for thumnail in thumnails:
    img = thumnail['src']
    dload.save(img, f'img/{i}.jpeg')
    i += 1

print('Success')

driver.quit() # 끝나면 닫아주기