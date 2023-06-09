import json
from typing import Dict

import requests

status = 'available'
header = {'accept': 'application/json', 'Content-Type': 'application/json'}
body_pet = {
      "id": 12101,
      "category": {
        "id": 131,
        "name": "Dog"
      },
      "name": "dog",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
body_pet1 = {
      "id": 12101,
      "category": {
        "id": 131,
        "name": "Cat"
      },
      "name": "cat",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
# Поиск питомцев по статусу
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers=header)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# Создаем питомца с помощью POST запроса
res = requests.post(f'https://petstore.swagger.io/v2/pet', data=json.dumps(body_pet), headers=header)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# # # # #Изменяем данные о питомце с помощью PUT запроса
res = requests.put(f'https://petstore.swagger.io/v2/pet', data=json.dumps(body_pet1), headers=header)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# Проверяем изменения с помощью GET запроса по его id
res = requests.get(f'https://petstore.swagger.io/v2/pet/12101', headers=header)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# Удаляем питомца с помощью запроса DELET по его id
res = requests.delete(f'https://petstore.swagger.io/v2/pet/12101', headers=header)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# Проверяем удаление с помощью GET запроса по его id
res = requests.get(f'https://petstore.swagger.io/v2/pet/12101', headers=header)
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
