from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/Users/maengbook/Desktop/driver/chromedriver')
driver.implicitly_wait(3)

url = 'https://wrightbrothers.kr/shop/bicycles/bicycles/?filter=%5B%22categoryTypes_%EB%A1%9C%EB%93%9C%EC%9E%90%EC%A0%84%EA%B1%B0_%EB%A1%9C%EB%93%9C%22%2C%22productStatus_P02_%EC%A4%91%EA%B3%A0%22%5D'

driver.get(url)
home = driver.page_source

soup_home = BeautifulSoup(home, 'html.parser')
number = soup_home.find('div','search-count')
last_number = int(number.h5.span.text)

data = []
for i in range(2,4):
    driver.find_element_by_xpath(f'//*[@id="body-content"]/div[2]/section/div/div/div/div[2]/div/div/div/div/div[2]/div/div[{i}]/div/div/a').click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    brand = soup.find('h2', class_='product-detail-title').a.text
    price = soup.find('div', class_='col-12').span.text.strip()
    keys = soup.find_all('h5', class_= 'mt-0 mb-1')
    values = soup.find_all('p', class_ = 'mb-0')
    driver.back()
    keys_list = []
    keys_list.extend(['브랜드', '가격'])
    values_list = []
    values_list.extend([brand, price])

    for key,value in zip(keys,values):
        keys_list.append(key.text.strip())
        values_list.append(value.text.strip())
    bike = {k:v for k,v in zip(keys_list, values_list)}
    data.append(bike)