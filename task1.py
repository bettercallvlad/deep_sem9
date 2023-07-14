# Задача №1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль
# просит угадать загаданное число за указанное число попыток.
from random import randint

def guessing_game(num: int, count: int) -> callable:
    def game() -> bool:
        for _ in range(count):
            user_number = int(input('Введите число: '))
            if user_number == num:
                print('Угадали')
                return True
            elif user_number < num:
                print('Число больше')
            else:
                print('Число меньше')
        print('Попытки кончились')
        return False

    return game


# game_test = guessing_game(10, 3)
# game_test()


# Задача №2
# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа
# в диапазоны [1, 100] и [1, 10]. Если не входят,
# вызывать функцию со случайными числами из диапазонов.

LOVER_LIMIT_TRIES = 1
UPPER_LIMIT_TRIES = 10
LOVER_LIMIT_NUM = 1
UPPER_LIMIT_NUM = 100


def game_decorator(func: callable) -> callable:

    def wrapper(num: int, count: int, *args, **kwargs) -> bool:
        if num < LOVER_LIMIT_NUM or num > UPPER_LIMIT_NUM:
            num = randint(LOVER_LIMIT_NUM, UPPER_LIMIT_NUM)
        if count < LOVER_LIMIT_TRIES or count > UPPER_LIMIT_TRIES:
            count = randint(LOVER_LIMIT_TRIES, UPPER_LIMIT_TRIES)
        return func(num, count)
    return wrapper


@game_decorator
def game_w_dec(num: int, count: int) -> bool:
    for _ in range(count):
        user_number = int(input('Введите число: '))
        if user_number == num:
            print('Угадали')
            return True
        elif user_number < num:
            print('Число больше')
        else:
            print('Число меньше')
    print('Попытки кончились')
    return False


game_w_dec(10, 3)
