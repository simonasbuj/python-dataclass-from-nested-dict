from dataclasses import dataclass, fields, is_dataclass
from typing import Any, Type, TypeVar, List, get_origin, get_args

T = TypeVar('T')

def create_dataclass_object_from_dict(cls: Type[T], data: dict) -> T:
    """
    Create a dataclass object from a dictionary, handling nested dataclasses and lists of dataclasses.
    """
    if not is_dataclass(cls):
        raise ValueError(f"{cls} is not a dataclass")

    field_values = {}
    for field in fields(cls):
        field_value = data.get(field.name)
        if field_value is not None:
            field_type = field.type
            if is_dataclass(field_type):
                field_value = create_dataclass_object_from_dict(field_type, field_value)
            elif get_origin(field_type) is list and is_dataclass(get_args(field_type)[0]):
                field_value = [create_dataclass_object_from_dict(get_args(field_type)[0], item) for item in field_value]
        field_values[field.name] = field_value

    return cls(**field_values)


@dataclass
class YetAnotherConfig:
    key: str
    value: Any

@dataclass
class Config:
    name: str
    yet_another_config_list: List[YetAnotherConfig]

# Example usage
data = {
    'name': 'example',
    'yet_another_config_list': [
        {'key': 'key1', 'value': 'value1'},
        {'key': 'key2', 'value': 'value2'}
    ]
}

config = create_dataclass_object_from_dict(Config, data)
print(config)