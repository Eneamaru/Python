from functools import wraps


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(x):
            if not callback(x):
                raise ValueError(f'Число "{x}" не может быть возведено в куб.')
            return func(x)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(2))
print(calc_cube(15))
print(calc_cube(-9))
