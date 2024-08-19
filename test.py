# Импортируем модули
import json
# Создаем тестовую функцию
def load() -> dict:
    """
    Функция для загрузки информации из файла в переменную.
    """
    with open("client_info.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
# Создаем глобальную переменную и загружаем в нее информацию
data = load()
# Выполняем задания
print(type(data))

print(data['name'])
print(data['accounts'][0]['balance'])

for dict in data['transactions']:
    if dict['type'] == "списание":
        print(f"Списано {dict['amount']} рублей.")
    elif dict['type'] == "зачисление":
        print(f"Зачислено {dict['amount']} рублей.")

data['name'] = "Иван Иванович"
print(data['name'])
# Сохраняем изменения в файл
with open("client_info.json", "w", encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False)