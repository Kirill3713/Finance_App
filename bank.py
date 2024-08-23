# Импортируем модули и создаем необходимые переменные
import json
import colorama
import random
client_info = {}
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
colors = [green, red, light_blue, light_cyan, light_green, light_magenta, light_red, light_white, light_yellow]
# Создаем функции
def suggestion() -> None:
    """
    Печатаем предложения банка.
    """
    with open("suggestions.txt", "r", encoding='utf-8') as txt_file:
        for line in txt_file:
            print(random.choice(colors) + line + reset, end="")

def feedback() -> None:
    """
    Функция для запроса отзыва.
    """
    text = input(light_cyan + "\nПожалуйста, введите отзыв: " + light_green)
    with open("client_info.json", "r", encoding='utf-8') as json_file:
        global client_info
        client_info = json.load(json_file)
    name = client_info["name"]
    with open("feedbacks.txt", 'a', encoding='utf-8') as txt_file:
        txt_file.write(f"{name}: {text}\n")
    print(light_green + "Отзыв успешно добавлен!" + reset)
# Точка входа
if __name__ == "__main__":
    suggestion()
    feedback()