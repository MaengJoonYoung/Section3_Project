from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/Users/maengbook/Desktop/driver/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)

# 중고 url
# url = 'https://wrightbrothers.kr/shop/bicycles/bicycles/?filter=%5B%22categoryTypes_%EB%A1%9C%EB%93%9C%EC%9E%90%EC%A0%84%EA%B1%B0_%EB%A1%9C%EB%93%9C%22%2C%22productStatus_P02_%EC%A4%91%EA%B3%A0%22%5D'
# 인증 중고 url
url = 'https://wrightbrothers.kr/shop/bicycles/bicycles/?filter=%5B%22categoryTypes_%EB%A1%9C%EB%93%9C%EC%9E%90%EC%A0%84%EA%B1%B0_%EB%A1%9C%EB%93%9C%22,%22productStatus_P03_%EB%9D%BC%EB%B8%8C%EC%9D%B8%EC%A6%9D%22%5D'

driver.get(url)
home = driver.page_source

# 사이트 내 총 제품개수
soup_home = BeautifulSoup(home, 'html.parser')
number = soup_home.find('div','search-count')
last_number = int(number.h5.span.text)

# 스크롤 내리기
prev_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.implicitly_wait(30)
    curr_height = driver.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

datas = []
for i in range(2,last_number+2):
    try:
        # 제품 클릭.
        driver.find_element_by_xpath(f"//*[@id='body-content']/div[2]/section/div/div/div/div[2]/div/div/div/div/div[2]/div/div[{i}]/div/div/a").click()
        driver.implicitly_wait(30)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # 자전거 브랜드
        brand = soup.find(class_='product-detail-title').text
        # 자전거 가격
        price = soup.find('div', class_='col-12').span.text.strip()
        # 브랜드와 가격 이외에 제품 스펙
        keys = soup.find_all('h5', class_= 'mt-0 mb-1')
        values = soup.find_all('p', class_ = 'mb-0')
    except:
        driver.back()
    keys_list = []
    keys_list.extend(['브랜드', '가격'])
    values_list = []
    values_list.extend([brand, price])
    for key,value in zip(keys[:10],values[:10]):
        keys_list.append(key.text.strip())
        values_list.append(value.text.strip())
    # 제품 스팩과 정보 딕셔너리 형태로 저장.
    bike = {k:v for k,v in zip(keys_list, values_list)}
    datas.append(bike)
    # 뒤로 가기
    driver.back()
    # 다음 제품 클릭할 수 있을때 까지 기다리기.
    elem = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='body-content']/div[2]/section/div/div/div/div[2]/div/div/div/div/div[2]/div/div[{i+1}]/div/div/a")))
    

driver.quit()
print(len(datas))

# 데이터 부호화
with open('data_2.pkl', 'wb') as pickle_file:
    pickle.dump(datas, pickle_file)