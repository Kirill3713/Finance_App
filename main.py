# Импортируем модули, отключаем предупреждения, очищаем экран и создаем переменные цветов
import os
import colorama
from bank import *
from plot import *
from client import *
import warnings
warnings.filterwarnings("ignore")
os.system("cls")
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
cyan = colorama.Fore.CYAN
light_yellow = colorama.Fore.LIGHTYELLOW_EX
light_blue = colorama.Fore.LIGHTBLUE_EX
light_cyan = colorama.Fore.LIGHTCYAN_EX
black = colorama.Fore.BLACK
light_white = colorama.Fore.LIGHTWHITE_EX
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
light_green = colorama.Fore.LIGHTGREEN_EX
light_red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
# Создаем меню
menu = light_white + """
1 - провести транзакцию
2 - посмотреть информацию о счетах
3 - добавление карты
4 - переименовать карту
5 - удалить карту
6 - посмотреть прогноз расходов и доходов
7 - посмотреть предложения банка
8 - оставить отзыв

Посмотреть курс:
9 - евро к доллару
10 - рубля к доллару
11 - евро к венгерскому форинту
12 - юань к доллару
13 - индийской рупии к доллару
14 - южноафриканского ранда к доллару

15 - выйти из программы
""" + reset
print(menu)
action = input(light_cyan + "Выберите действие: " + light_green)
# Запуск основного цикла
while action != "15":
    if action in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
        if action == "1":
            add_transaction()
        if action == "2":
            show_info()
        if action == "3":
            add_card()
        if action == "4":
            rename_card()
        if action == "5":
            delete_card()
        if action == "6":
            predict()
        if action == "7":
            suggestion()
        if action == "8":
            feedback()
        if action == "9":
            plot_euro_usd()
        if action == "10":
            plot_rub_usd()
        if action == "11":
            plot_eur_huf()
        if action == "12":
            plot_cyn_usd()
        if action == "13":
            plot_inr_usd()
        if action == "14":
            plot_zar_usd()

    else:
        print(red + "Нет такого действия!" + reset)

    input(blue + "Нажмите Enter чтобы продолжить. " + light_blue)
    os.system("cls")
    print(menu)
    action = input(light_cyan + "Выберите действие: " + light_green)
print(cyan + "Спасибо за использование нашей программы!")