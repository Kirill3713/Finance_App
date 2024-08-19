# Импортируем нужные модули и создаем переменные цветов
import json
import datetime
import random
import colorama
reset = colorama.Fore.RESET
light_blue = colorama.Fore.LIGHTBLUE_EX
light_white = colorama.Fore.LIGHTWHITE_EX
white = colorama.Fore.WHITE
cyan = colorama.Fore.CYAN
light_cyan = colorama.Fore.LIGHTCYAN_EX
light_green = colorama.Fore.LIGHTGREEN_EX
light_red = colorama.Fore.LIGHTRED_EX
red = colorama.Fore.RED
black = colorama.Fore.BLACK
# Объявляем глобальную переменную, где будут храниться данные пользователя
client_info = {}
# Создаем функции
def load() -> None:
    """
    Переписываем переменную, добавляя в нее данные.
    """
    with open("client_info.json", "r", encoding='utf-8') as json_file:
        global client_info
        client_info = json.load(json_file)

def save() -> None:
    """
    Функция для сохранения данных из переменной в файл.
    """
    with open("client_info.json", "w", encoding='utf-8') as json_file:
        global client_info
        json.dump(client_info, json_file, ensure_ascii = False)

def show_info() -> None:
    """
    Вывод информации о счетах.
    """
    print(light_white + "==================================" + reset)
    print(cyan + "Информация о счетах:" + reset)
    print(light_white + "==================================" + reset)
    global client_info
    for accounts in client_info["accounts"]:
        print(light_blue + f"Название карты: {accounts["name"]}" + reset)
        print(white + "----------------------------------" + reset)
        print(light_blue + f"Система: {accounts["system"]}" + reset)
        print(white + "----------------------------------" + reset)
        print(light_blue + f"Номер карты: {accounts["number"]}" + reset)
        print(white + "----------------------------------" + reset)
        print(light_blue + f"Тип карты: {accounts["type"]}"+ reset)
        print(white + "----------------------------------" + reset)
        print(light_blue + f"Баланс на карте: {accounts["balance"]}" + reset)
        print(white + "----------------------------------" + reset)
        print(light_blue + f"Срок годности: {accounts["validity period"]}" + reset)
        print(light_white + "==================================" + reset)

def predict() -> None:
    """
    Функция для предсказания расходов и доходов.
    """
    # Объявляем переменные доходов, расходов и списка месяцев
    expences = 0
    incom = 0
    months = []
    global client_info
    # Создаем список месяцев
    for transaction in client_info["transactions"]:
        if not transaction["date"] in months:
            months.append(transaction["date"])
    # Подсчитываем все доходы и расходы (привет от очень состоятельных кротов))
    for transaction in client_info["transactions"]:
        if transaction["type"] == 'списание':
            expences += transaction["amount"]
        elif transaction["type"] == 'зачисление':
            incom += transaction["amount"]
    # Выводим прогноз
    print(light_cyan + f"Ваши предпологаемые расходы в следующем месяце: {expences // len(months)},\nВаши предпологаемые доходы в следующем месяце: {incom // len(months)}." + reset)

def add_transaction() -> None:
    """
    Функция, осуществляющая транзакции.
    """
    global client_info
    # Выводим информацию о картах пользователя
    print(light_cyan + "Досупные счета:" + reset)
    show_info()
    a = 1
    for card in client_info["accounts"]:
        print(cyan + f"{a}. {card["name"]}" + reset)
        a += 1
    # Спрашиваем у пользвателя номер карты
    number_from_list = input(light_cyan + "С какой карточки Вы хотите провести транзакцию? Выберите номер из списка выше: " + light_green).strip()
    numbers = []
    # Создаем список номеров карт и ищем номер нужной карты и добавляем исключения
    for account in client_info["accounts"]:
        numbers.append(account["number"])
    try:
        number_of_card = client_info["accounts"][int(number_from_list)-1]["number"]
    except IndexError:
        print(light_red + "Введено некорректное значение!" + reset)
        return
    except ValueError:
       print(light_red + "Введено некорректное значение!" + reset)
       return
    if number_from_list == "0":
       print(light_red + "Введено некорректное значение!" + reset)
       return
    # Если у пользователя нет такой карты, то останавливаем операцию.
    if not number_of_card in numbers:
        print(light_red + "Ошибка! У Вас нет карты с таким номером! Транзакция прервана!" + reset)
        return
    # Запрашиваем тип операции и добавляем ошибку
    action = input(light_cyan + "Вы хотите перечислить деньги с Вашей карты на Вашу (1) или перечислить с Вашей на другую карту (2)? (нужно ввести номер) " + light_green).strip()
    if not action in ["1", "2"]:
        print(light_red + "Ошибка! Некорректный ввод! Транзакция прервана!" + reset)
        return
    # Собираем информацию о дате проведения транзакции
    date = {"year": datetime.datetime.now().year, "month": datetime.datetime.now().month}
    # Запрашиваем у пользователя размер транзакции и добавляем исключения
    amount = input(light_cyan + "Сколько Вы хотите перечислить? " + light_green).strip()
    try:
        amount = int(amount)
    except ValueError:
        print(light_red + "Ошибка! Некорректный ввод! Транзакция прервана!" + reset)
        return
    for card in client_info["accounts"]:
        if number_of_card == card["number"]:
            card = card
            break
    if card["balance"] < amount:
        print(light_red + "Недостаточно средств!" + reset)
        return
    # Добавляем транзакцию в client_info
    if action == "1":
        a = 1
        for card in client_info["accounts"]:
            print(cyan + f"{a}. {card["name"]}" + reset)
            a += 1
        # Спрашиваем у пользователя номер карты
        number_from_list2 = input(light_cyan + "На какую карту Вы хотите перечислить деньги? Выберите номер из списка выше: " + light_green).strip()
        numbers = []
        # Создаем список номеров карт и ищем номер нужной карты
        for account in client_info["accounts"]:
            numbers.append(account["number"])
        try:
            number_of_card2 = client_info["accounts"][int(number_from_list2)-1]["number"]
        except IndexError:
            print(light_red + "Введено некорректное значение!" + reset)
            return
        except ValueError:
            print(light_red + "Введено некорректное значение!" + reset)
            return
        if number_from_list == "0":
            print(light_red + "Введено некорректное значение!" + reset)
            return
        type_of_transaction = "перечисление"
        # Если у пользователя нет такой карты, то останавливаем операцию.
        if not number_of_card2 in numbers:
            print(light_red + "Ошибка! У Вас нет карты с таким номером! Транзакция прервана!" + reset)
            return
    else:
        type_of_transaction = "списание"
        check = input(light_cyan + "Введите номер карты, на которую хотите перечислить деньги: " + light_green).strip().replace(" ", "")
        # Проверяем номер на правильность
        try:
            int(check)
        except ValueError:
            print(light_red + "Введено некорректное значение!" + reset)
            return
        symbs = 0
        for symb in str(check):
            symbs += 1
        if symbs != 16:
            print(light_red + "Введено некорректное значение!" + reset)
            return
    transaction = {
            "account": number_of_card,
            "type": "списание",
            "date": date,
            "amount": amount
            }
    if action == "1":
        transaction2 = {
                "account": number_of_card2,
                "type": "зачисление",
                "date": date,
                "amount": amount
                }
        client_info["transactions"].append(transaction2)        
    
    client_info["transactions"].append(transaction)
    # Проводим операцию
    index = 0
    for card in client_info["accounts"]:
        if card["number"] == number_of_card:
            client_info["accounts"][index]["balance"] -= amount
        if action == "1":
            if card["number"] == number_of_card2:
                client_info["accounts"][index]["balance"] += amount
        index += 1
    # Сохраняем в файл
    save()
    print(light_green + "Транзакция прошла успешно!" + reset)

def add_card() -> None:
    """
    Функция для создания новой карты
    """
    # Собираем данные для карты
    # Имя и система карты
    name = input(light_cyan + "Введите название новой карты: " + light_green)
    names = []
    # Создаем список имен карт
    for account in client_info["accounts"]:
        names.append(account["name"])
    # Если у пользователя есть такая карта, то останавливаем операцию.
    if name in names:
        print(light_red + "Ошибка! У Вас уже есть карта с таким названием! Операция прервана!" + reset)
        return
    system = input(light_cyan + "Введите карту какой системы Вы хотите завести (например мастеркард или виза) " + light_green)
    numbers = []
    # Создаем уникальный номер карты
    for account in client_info["accounts"]:
        numbers.append(account["number"])
    number = random.randint(1000000000000000, 9999999999999999)
    number = str(number)
    number = f"{number[0:4]} {number[5:9]} {number[9:13]} {number[12:16]}"
    while number in numbers:
        number = random.randint(1000000000000000, 9999999999999999)
        number = str(number)
        number = f"{number[0:4]} {number[5:9]} {number[9:13]} {number[12:16]}"
    print(light_cyan + f"Номер Вашей карты: {number}" + reset)
    # Тип карты
    type_of_card = input(light_cyan + "Введите карту какого типа Вы хотите завести: дебетовую (1) или кредитную (2)? " + light_green).strip()
    if type_of_card == "1":
        type_of_card = "дебетовая"
    elif type_of_card == "2":
        type_of_card = "кредитная"
    else:
        print(light_red + "Некорректный ввод! Операция прервана! Требуется перезапуск программы!" + reset)
        return
    # Срок годности карты
    validity_period = datetime.datetime.today() + datetime.timedelta(days=365)
    validity_period = str(validity_period).split()
    validity_period = validity_period[0].split("-")
    validity_period = f"{validity_period[1]}/{validity_period[0]}"
    print(light_cyan + f"Срок годности Вашей карты закончится {validity_period}." + reset)
    # Проверка   
    print(light_cyan + "Данные Вашей новой карты:" + light_green)
    for i in range(3):
        correction = input(light_white + f"""
        Название карты: {name},
        Система: {system},
        Номер карты: {number},
        Тип карты: {type_of_card},
        Нынешний баланс: 0,
        Срок годности: {validity_period}.
        
        Если все введено верно нажмите 0,
        Если Вы хотите изменить имя карты нажмите 1,
        Если Вы хотите изменить систему карты нажмите 2,
        Если Вы хотите изменить тип карты нажмите 3,
        Если Вы хотите отменить операцию нажмите 10.
        """ + light_green).strip()
        if correction == "0":
            break
        elif correction == "1":
            name = input(light_cyan + "Введите новое название карты: " + light_green)
        elif correction == "2":
            system = input(light_cyan + "Введите другую систему (примечание, дальнейшее изменнение системы невозможно!): " + light_green)
        elif correction == "3":
                type_of_card = input(light_cyan + "Введите карту какого типа Вы хотите завести (примечание, дальнейшее изменнение типа карты невозможно!): дебетовую (1), кредитную (2)? " + light_green)
                if type_of_card == "1":
                    type_of_card = "дебетовая"
                elif type_of_card == "2":
                    type_of_card = "кредитная"
        elif correction == "10":
            confirmation = input(light_cyan + "Вы уверены, что хотите сбросить операцию? Если да, то введите 1. " + light_green)
            if confirmation == "1":
                return
    # Создаем словарь со всеми данными карты
    card_info = {
        "name": name,
        "system": system,
        "number": number,
        "type": type_of_card,
        "balance": -100,
        "validity period": validity_period
    }
    print(black + "Карта стоит 100 рублей." + reset)
    # Добавляем и сохраняем карту и выводим уведомление об успешном завершении операции
    client_info["accounts"].append(card_info)
    save()
    print(light_green + "Карта успешно добавлена!" + reset)

def rename_card() -> None:
    """
    Функция, позволяющая переименовать карту.
    """
    global client_info
    # Выводим информацию о картах пользователя
    print(light_cyan + "Досупные счета:" + reset)
    show_info()
    a = 1
    for card in client_info["accounts"]:
        print(cyan + f"{a}. {card["name"]}" + reset)
        a += 1
    # Спрашиваем у пользвателя номер карты
    number_from_list = input(light_cyan + "Какую карту Вы хотите переименовать? Выберите номер из списка выше: " + light_green).strip()
    try:
        old_name = client_info["accounts"][int(number_from_list)-1]["name"]
    except IndexError:
        print(light_red + "Введено некорректное значение!" + reset)
        return
    except ValueError:
       print(light_red + "Введено некорректное значение!" + reset)
       return
    if number_from_list == "0":
       print(light_red + "Введено некорректное значение!" + reset)
       return
    new_name = input(light_cyan + "Введите новое название карты: " + light_green)
    names = []
    # Создаем список имен карт
    for account in client_info["accounts"]:
        names.append(account["name"])
    # Если у пользователя есть такая карта, то останавливаем операцию.
    if new_name in names:
        print(light_red + "Ошибка! У Вас уже есть карта с таким названием! Операция прервана!" + reset)
        return
    confirmation = input(light_cyan + f"Вы хотите переименовать карту с номером {client_info["accounts"][int(number_from_list)-1]["number"]} на {new_name}? Предыдущее имя: {old_name}. Чтобы подтвердить введите 1. " + light_green).strip()
    if confirmation == "1":
        client_info["accounts"][int(number_from_list)-1]["name"] = new_name
        save()
        print(light_green + "Карта успешно переименована!" + reset)

def delete_card() -> None:
    """
    Функция для удаления карты.
    """
    global client_info
    # Выводим информацию о картах пользователя
    print(light_cyan + "Досупные счета:" + reset)
    show_info()
    a = 1
    for card in client_info["accounts"]:
        print(cyan + f"{a}. {card["name"]}" + reset)
        a += 1
    # Спрашиваем у пользвателя номер карты
    number_from_list = input(light_cyan + "Какую карту Вы хотите удалить? Выберите номер из списка выше: " + light_green).strip()
    try:
        info = client_info["accounts"][int(number_from_list)-1]
    except IndexError:
        print("Введено некорректное значение!")
        return
    except ValueError:
       print(light_red + "Введено некорректное значение!" + reset)
       return
    if number_from_list == "0":
       print(light_red + "Введено некорректное значение!" + reset)
       return
    # Віводим информацию об удаляемой карте
    print(light_white + "==================================" + reset)
    print(light_blue + f"Название карты: {info["name"]}" + reset)
    print(white + "----------------------------------" + reset)
    print(light_blue + f"Система: {info["system"]}" + reset)
    print(white + "----------------------------------" + reset)
    print(light_blue + f"Номер карты: {info["number"]}" + reset)
    print(white + "----------------------------------" + reset)
    print(light_blue + f"Тип карты: {info["type"]}"+ reset)
    print(white + "----------------------------------" + reset)
    print(light_blue + f"Баланс на карте: {info["balance"]}" + reset)
    print(white + "----------------------------------" + reset)
    print(light_blue + f"Срок годности: {info["validity period"]}" + reset)
    print(light_white + "==================================" + reset)
    # Пользователь подтверждает, что он хочет удалить карту
    confirmation = input(light_red + "Вы точно хотите удалить эту карту? Все данные И СРЕДСТВА на карте НЕЛЬЗЯ БУДЕТ ВЕРНУТЬ!!! Для подтверждения введите 1. " + red)
    if confirmation == "1":
        del client_info["accounts"][int(number_from_list)-1]
    else:
        print(white + "Удаление сброшено." + reset)
    save()
    print(black + "Карта успешно удалена." + reset)

load()
# # Точка входа
# if __name__ == "__main__":
#     # show_info()
#     # predict()
#     # add_transaction()
#     # add_card()
#     # rename_card()
#     # delete_card()
#     # save()