'''
---
layout: single
title:  "첫 포스팅입니다. 설렘 가득하네요."
---
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from pandas import DataFrame
import re
import time

df = pd.read_excel(r'C:\Users\USER\Desktop\ybs관련문서\T-MAP\POI_취합_ybs검토_20220820.xlsx',sheet_name='강원도 읍면동_행안부')

url = 'https://map.yjhoon.com/naver/'
driver = webdriver.Chrome('C:/data/chromedriver.exe')
driver.get(url)


j = 0
for i in df['주소']:      
    try:
        element = driver.find_element(By.CSS_SELECTOR,'div.search > form > input')
        text = ''
        element.clear()
        time.sleep(2)
        element.send_keys(i)
        time.sleep(2)
        element2 = driver.find_element(By.CSS_SELECTOR,'div.search > form > button.btn').click()
        time.sleep(3)
        text = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]').text
        time.sleep(3)
        df['X좌표'][j] = re.findall('[0-9]+.[0-9]+',re.findall('X좌표 : [0-9]+\.[0-9]+',text)[0])[0]
        df['Y좌표'][j] = re.findall('[0-9]+.[0-9]+',re.findall('Y좌표 : [0-9]+\.[0-9]+',text)[0])[0]
        
        time.sleep(3)
        j = j+1
        time.sleep(5) 
        
    except:
        j = j+1
        print(i,': 이 주소는 좌표를 따로 찾아야합니다. 검색이 되지 않습니다.')
        continue
        

df.to_excel(r'C:\Users\USER\Desktop\T-MAP\좌표.xlsx')
