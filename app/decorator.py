from typing import Callable

def fence(func: Callable) -> Callable:
    def wrapper():
        print('+' * 10)
        func()
        print('+' * 10)
    return wrapper

@fence
def say_hello() -> None:
    print("Hello, Decorators!")

say_hello()

def custom_fence(border_char: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper() -> None:
            print(border_char * 10)
            func()
            print(border_char * 10)
        return wrapper
    return decorator

@custom_fence('-')
def say_goodbye() -> None:
    print("Goodbye, Decorators!")

say_goodbye()

def custom_fence_with_arg(border_char: str) -> Callable:
    def decorator(func: Callable[[str], None]) -> Callable:
        def wrapper(name: str) -> None:
            print(border_char * len(name))
            func(name)
            print(border_char * len(name))
        return wrapper
    return decorator

@custom_fence_with_arg('*')
def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("Alice")