# Задача №3
# Напишите декоратор, который сохраняет в json файл параметры
# декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать
# как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json


def json_cache(func: callable) -> callable:
    with open(f"{func.__name__}.json", 'r') as log:
        data = json.load(log)

    def wrapper(*args, **kwargs) -> None:
        temp_dict = {'args': args, 'kwargs': kwargs, 'result': func(*args, **kwargs)}
        data.append(temp_dict)
        with open(f"{func.__name__}.json", 'w') as log:
            json.dump(data, log, indent=4)

    return wrapper


@json_cache
def test(*args, **kwargs):
    return sum(args)


test(111, 555, 333, text="TRUE", img='png.png')