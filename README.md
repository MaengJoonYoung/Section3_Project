# Section3_Project

중고 자전거 가격을 예측하는 머신러닝 모델 구축 후 웹 서비스로 배포.

<br>

<img width="904" alt="중고자전거" src="https://user-images.githubusercontent.com/89771322/161058686-e82726ac-2af3-4388-b0e4-d5522f0b5f81.png">

<br>

## 문제 정의 

자전거를 구매하려고 할때 브랜드 종류, 소재, 구동계 등 고려해야할 것들이 많기 때문에 자전거를 처음 구매하는 사람들의 경우 굉장히 막막하다는 문제가 있다. 

<br>

자신이 원하는 스펙의 자전거를 입력하고 예측 가격을 확인하는 방식으로 자전거를 처음 구매하는 사람들에게 도움이 되고자 프로젝트를 계획.

<br>

## 폴더 & 파일 <br>

### 트리구조 <br>


```
├── Preprocessing&model_test.ipynb
├── Procfile
├── README.md
├── Used_bicycle
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── scraping.cpython-38.pyc
│   ├── add.py
│   ├── model.py
│   ├── scraping.py
│   └── templates
│       ├── cover.css
│       ├── index.html
│       └── predict.html
├── bicycle.csv
├── data.pkl
├── data_2.pkl
├── model_2.pkl
├── requirements.txt
└── used_bicycle.db
```

### 파일 설명 <br>

- `scraping.py` : 동적 크롤러
- `add.py` : DB에 데이터 적재
- `model.py` : 모델 훈련
- `model_2.pkl` : XGB Regressor 모델
- `data_2.pkl, data,pkl` : dictionary 형태의 데이터
- `Preprocessing&model_test.ipynb` : 전처리 및 모델 성능 비교

<br>

## 진행 과정

1. selenium, SQLite 활용하여 동적 크롤링 후 DB에 데이터 적재.
2. pandas, numpy, matplotlib 활용하여 EDA 및 전처리 진행.
3. sklearn 활용하여 0.72의 R2 score를 가진 XGB Regressor 모델 구축.
4. Metabase 활용하여 대시보드 제작.
5. Flask로 웹 어플리케이션 제작 후 Heroku로 배포.

<br>

## 결과물
[중고 자전거 가격 예측](https://usedbicycle.herokuapp.com/)

<br>

## 한계점

1. Metabase로 만든 대시보드를 웹 페이지에 같이 게시했다면, 사용자의 편의를 더욱 늘릴 수 있을 것 같았지만, 시간 관계상 하지 못했다.
2. 모델이 충분히 학습하기에는 데이터 개수가 부족했다고 생각.
