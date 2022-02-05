from functools import wraps


def wrapper(func):
    @wraps(func)
    def _wrapper(*args):
        logs = [f'{func.__name__}({el}: {type(el)})' for el in args]
        result = [func(el) for el in args]
        print(logs)
        return result
    return _wrapper


@wrapper
def calc_cube(x):
    return x ** 3


print(calc_cube(3, 7, 11))
