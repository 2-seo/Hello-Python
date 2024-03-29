# 파이썬 패키지 사용하기
# dload

import dload
# 이미지 저장
# dload.save("https://spartacodingclub.kr/static/css/images/ogimage.png")

# 셀레니움 selenium -> 브라우저를 자동 제어
# https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.87/

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

thumnails = soup.select('#imgList > div > a > img')

i = 1;
for thumnail in thumnails:
    img = thumnail['src']
    dload.save(img, f'img/{i}.jpg')
    i += 1


driver.quit() # 끝나면 닫아주기