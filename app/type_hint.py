from typing import Any

num : int = 42
text : str = "Hello, World!"
digits : list[int] = [1, 2, 3, 4, 5]
city_temp : tuple[str, float] = ("New York", 22.5)
nums : tuple[int, ...] = (1, 2, 3, 4, 5)
data_dict : dict[str, Any] = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
mixed_list : list[Any] = [1, "two", 3.0, True, None]

def root(num : int | float, exp : float | None = 0.5) -> float:
    return pow(num, exp)