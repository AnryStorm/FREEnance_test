import requests

url = 'https://freenance.online/rectangle/mainfieldcosts'

# Отправляем GET-запрос на указанный URL
response = requests.get(url)

# Проверяем статус-код ответа
if response.status_code == 200:
    print("Страница успешно загружена")
else:
    print("Ошибка при загрузке страницы")

# Проверяем содержимое страницы на наличие ожидаемых элементов
expected_elements = ['<h1>Rectangle Main Field Costs</h1>',
                     '<form method="POST" action="/rectangle/mainfieldcosts">',
                     '<input type="number" name="width" placeholder="Width">',
                     '<input type="number" name="height" placeholder="Height">',
                     '<button type="submit">Calculate</button>']

for element in expected_elements:
    if element in response.text:
        print(f"Элемент '{element}' найден на странице")
    else:
        print(f"Элемент '{element}' не найден на странице")
