#네이버 쇼핑에서 혼다 125CC 긁어 오는 코드 크롤링 
# 정리
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

# chromedriver 위치에서 코드작업 필수 
chrome_options = Options()
driver = webdriver.Chrome(service=Service('/User/chromedriver'), options=chrome_options)
URL = 'https://search.shopping.naver.com/search/all?frm=PCX&origQuery=PCX&pagingIndex=1&pagingSize=40&productSet=total&query=pcx125&sort=review&timestamp=&viewType=list'
driver.get(URL)

soup = BeautifulSoup(driver.page_source, 'html.parser')
goods_list = soup.select('li.basicList_item__0T9JD')

# list들
list_name = []
list_price = []
list_date = []
list_seller = []
list_img = []
list_url = []

for v in goods_list:
    item_name = v.select_one('div.basicList_title__VfX3c > a').get('title')
    list_name.append(item_name)
    item_price = v.select_one('strong.basicList_price__euNoD > span').text
    list_price.append(item_price)
    item_date = v.select_one('div.basicList_etc_box__5lkgg > span').text.split(' ')[1]
    list_date.append(item_date)
    if v.select_one('div.basicList_mall_title__FDXX5 > a > img') == None:
        item_seller = v.select_one('div.basicList_mall_title__FDXX5 > a').text
    else:
        item_seller = v.select_one('div.basicList_mall_title__FDXX5 > a > img').get('alt')
    list_seller.append(item_seller)
        
    item_URL = v.select_one('div.basicList_title__VfX3c > a').get('href')
    list_url.append(item_URL)
    
    
##driver.close() 웹사이트를 밑으로 긁어 줘야지 전체가 나옴 ..html문제

#2테이블로 정리
""" df = pd.DataFrame(
    {
        '상품명': list_name,
        '가격': list_price,
        '등록일': list_date,
        '판매자': list_seller,
        '상품 URL': list_url
    }
)
df """