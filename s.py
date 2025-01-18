from dataclasses import dataclass
from typing import Optional


@dataclass
class MyDataClass:
    name: str
    age: int
    is_active: bool = False

obj = MyDataClass(name='John', age=30)
print(obj)