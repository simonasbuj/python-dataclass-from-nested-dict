from dataclasses import dataclass, fields, is_dataclass, MISSING
from typing import Any, Optional, Type, TypeVar, get_origin, get_args


# Function to recursively convert dict to dataclass
T = TypeVar('T')
def create_dataclass_object_from_dict(cls: Type[T], data: dict) -> Any:
    """
    Create a dataclass object from a dictionary, handling nested dataclasses and lists of dataclasses.
    """
    if not is_dataclass(cls):
        raise ValueError(f"{cls} is not a dataclass")

    field_values = {}
    for field in fields(cls):
        field_value = data.get(field.name, MISSING)
        if field_value is MISSING:
            if field.default is not MISSING:
                field_value = field.default
            elif field.default_factory is not MISSING:
                field_value = field.default_factory()
            else:
                raise ValueError(f"Missing value for field '{field.name}' in {cls.__name__}")
        elif field_value is None:
            if field.default is MISSING and field.default_factory is MISSING:
                raise ValueError(f"Field '{field.name}' in {cls.__name__} cannot be None")
            else:
                continue  # Skip fields with None values if they have defaults

        field_type = field.type
        if is_dataclass(field_type):
            field_value = create_dataclass_object_from_dict(field_type, field_value)
        elif get_origin(field_type) is list and is_dataclass(get_args(field_type)[0]):
            field_value = [create_dataclass_object_from_dict(get_args(field_type)[0], item) for item in field_value]

        field_values[field.name] = field_value

    return cls(**field_values)


if __name__ == "__main__":
    # create dataclasses
    
    @dataclass 
    class OneMoreConfig:
        secret: str
        host: Optional[str] = "localhost"
        hi: Optional[int] = None

    @dataclass 
    class YetAnotherConfig:
        secret: Optional[str] = None

    # Nested dataclass for path
    @dataclass
    class PathConfig:
        base: str
        file: str
        one_more_config: OneMoreConfig

    # Main dataclass that includes PathConfig
    @dataclass
    class Config:
        bucket: str
        path: PathConfig
        yet_another_config: YetAnotherConfig
        yet_another_config_list: list[YetAnotherConfig]


    @dataclass
    class SimpleDataClass:
        name: str


    # Example dictionary
    config_dict = {
        "bucket": "my-bucket",
        "path": {
            "base": "my/full/path",
            "file": "some-file.parquet",
            "one_more_config": {
                "secret": "my_secret"
            }
        },
        "yet_another_config": {
            "secret": "goodbye"
        },
        "yet_another_config_list": [
            {
                "secret": "goodbye"
            },
            {
                "secrest": "goodbye"
            },
        ]
    }


    # Automatically create the Config dataclass from the dictionary
    config = create_dataclass_object_from_dict(Config, config_dict)
    simple_data_class: SimpleDataClass = create_dataclass_object_from_dict(SimpleDataClass, {"name": "mez"})

    print(config)
    print(simple_data_class)

