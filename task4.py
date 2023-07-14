# Задача №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

def counter(n: int):
    lst_counter = []

    def deco(func: callable):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                lst_counter.append(func(*args, **kwargs))
            return lst_counter
        return wrapper
    return deco


@counter(11)
def test(*args, **kwargs) -> int:
    return sum(args)


print(test(111, 222, 333))
