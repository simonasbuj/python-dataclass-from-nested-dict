from dataclasses import dataclass, fields, is_dataclass
from typing import Any, Optional, Type, TypeVar, Union



@dataclass 
class OneMoreConfig:
    secret: str
    host: Optional[str] = "localhost"
    hi: Optional[int] = None

@dataclass 
class YetAnotherConfig:
    secret: str

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


@dataclass
class SimpleDataClass:
    name: str


# Function to recursively convert dict to dataclass
T = TypeVar('T')
def create_dataclass_object_from_dict(dataclass_type: Type[T], dict_data: dict) -> Any:
    # Check if the type is a dataclass
    if is_dataclass(dataclass_type):
        # Get the dataclass fields
        fieldtypes = {f.name: f.type for f in fields(dataclass_type)}
        return dataclass_type(**{
            field: create_dataclass_object_from_dict(fieldtypes[field], dict_data[field])
            for field in dict_data
        })
    else:
        # If it's not a dataclass (primitive type), just return the value
        return dict_data


# Example dictionary
config_dict = {
    "bucket": "dwh",
    "path": {
        "base": "my/full/path",
        "file": "some-file.parquet",
        "one_more_config": {
            "secret": "my_secret"
        }
    },
    "yet_another_config": {
        "secret": "goodbye"
    }
}


# Automatically create the Config dataclass from the dictionary
config = create_dataclass_object_from_dict(Config, config_dict)
simple_data_class: SimpleDataClass = create_dataclass_object_from_dict(SimpleDataClass, {"name": "mez"})

print(config)
print(simple_data_class)

