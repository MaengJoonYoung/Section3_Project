from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

from bs4 import BeautifulSoup
import time

# options = webdriver.ChromeOptions()
# options.headless = True # headless Chrome 설정.
# options.add_argument("windos-size=2560x1600")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36")

driver = webdriver.Chrome('/Users/maengbook/Desktop/driver/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)

url = 'https://wrightbrothers.kr/shop/bicycles/bicycles/?filter=%5B%22categoryTypes_%EB%A1%9C%EB%93%9C%EC%9E%90%EC%A0%84%EA%B1%B0_%EB%A1%9C%EB%93%9C%22%2C%22productStatus_P02_%EC%A4%91%EA%B3%A0%22%5D'

driver.get(url)
home = driver.page_source

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

data = []
for i in range(2,last_number+2):
    try:
        driver.find_element_by_xpath(f"//*[@id='body-content']/div[2]/section/div/div/div/div[2]/div/div/div/div/div[2]/div/div[{i}]/div/div/a").click()
        driver.implicitly_wait(30)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        brand = soup.find(class_='product-detail-title').text
        price = soup.find('div', class_='col-12').span.text.strip()
        keys = soup.find_all('h5', class_= 'mt-0 mb-1')
        values = soup.find_all('p', class_ = 'mb-0')
        keys_list = []
        keys_list.extend(['브랜드', '가격'])
        values_list = []
        values_list.extend([brand, price])
        for key,value in zip(keys,values):
            keys_list.append(key.text.strip())
            values_list.append(value.text.strip())
        bike = {k:v for k,v in zip(keys_list, values_list)}
        data.append(bike)
        driver.back()
        # while True:
        #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #         driver.implicitly_wait(30)
        #         curr_height = driver.execute_script("return document.body.scrollHeight")
        #         if curr_height == prev_height:
        #             break
        #         prev_height = curr_height
        elem = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='body-content']/div[2]/section/div/div/div/div[2]/div/div/div/div/div[2]/div/div[{i+1}]/div/div/a")))
    except:
        pass

driver.quit()
print(len(data))

with open('data_2.pkl', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)