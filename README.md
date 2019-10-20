# bitrate

# Get Started
## 0. Устновка программы
  - Первым делом нужно устрановить Django и настроить PostgreSQL. 
## 1. Установка зависимостей
  - pip install psycopg2 - для работы с PostgreSQL
## 2. Migrate
  - python manage.py makemigrations
  - python manage.py migrate
## 3. Load Data
  Далее нужно загрузить данные по валютам. Команда автомтически загрузить валюты BTC, ETH, XRP, NEO и LTC
  - python manage.py loaddata currencies
## 4. Run Server
  - python manage.py runserver
  
# Поддержка страниц 
  - Get - /currencies/[?limit&page] - вернет список валют с возможностью пагинации. По умолчанию параметр limit = 10, page = 0
  - Get - /rate/<int:currency_id> - вернет последний курс валюты для переданного id и средний объем торгов за последние 10 дней
  
