import requests
import pandas as pd
import sqlite3
from Properties.db_paths import fdb_path

TOKEN = 'Q13N0A9-QJVMRR0-H4B7BCX-4C984BM'

min_rating = 8 # минимальный рейтинг искомых фильмов
max_rating = 10 # максимальный рейтинг искомых фильмов
limit = 250 # максимальное количество искомых фильмов (не более 250)
url_base = f'https://api.kinopoisk.dev/v1.4/movie'
url_params = f'?type=movie&rating.kp={min_rating}-{max_rating}&limit={limit}&votes.kp=10000-9999999999'
# url_params = f'?lists=top-250&limit={limit}'

headers = {'X-API-KEY': TOKEN}
response = requests.get(url_base + url_params, headers=headers)
movie_list = response.json()['docs']

movie_list[100]

data = []
for movie in movie_list:
  data.append([movie['name'], movie['rating']['kp'], movie['poster']['url']])

df = pd.DataFrame(data, columns=['name', 'rating', 'poster'])
conn = sqlite3.connect(fdb_path)
df.to_sql('Films', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
