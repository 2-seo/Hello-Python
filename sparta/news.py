from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('./chromedriver')

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D'

driver.get(url)
# time.sleep(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# 여기에 코드 적기!
#####################

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one('dl > dt > a')['title']
    news_url = article.select_one('dl > dt > a')['href']
    comp = article.select_one('dl > dd > span').text.split(' ')[0].replace('언론사', '')
    ws1.append([title, news_url, comp])

wb.save(filename='articles.xlsx')
driver.quit()