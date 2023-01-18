from fastapi import FastAPI
import requests

app = FastAPI()

# Укажите id игрока для поиска
variable = "57886125"
# Выберите stats или achievements
selects = "achievements"
# Спецификатор поиска - account_id
search = "account_id"
# Ключ доступа API
key = "214c61dc71b81996bedc15084ef9673f"

# Поиск техники в базе данных Lesta
response = requests.get(
url=f'https://api.tanki.su/wot/tanks/{selects}/?application_id={key}&{search}={variable}',
)
# Просматриваем значения атрибутов результатов поиска по базе Lesta
json_response = response.json()

#print(response.json())

@app.get ('/')
def home():
    return response.json()