def debug(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@debug
def add(a, b):
    return a + b

print(add(2, 3))