from dataclasses import dataclass
from typing import Optional
from nested_dataclass_from_dict import create_dataclass_object_from_dict


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



def test_create_dataclass_object_from_dict():
    # Example dictionary
    input_dict = {
        "bucket": "my-bucket",
        "path": {
            "base": "my/full/path",
            "file": "some-file.parquet",
            "one_more_config": {
                "secret": "my_secret"
            }
        },
        "yet_another_config": {
            "secrets": "goodbye"
        },
        "yet_another_config_list": [
            {
                "secret": "goodbye"
            },
            {
                "secret": "h"
            },
        ]
    }

    expected_object = Config(
        bucket='my-bucket', 
        path=PathConfig(
            base='my/full/path', 
            file='some-file.parquet', 
            one_more_config=OneMoreConfig(
                secret='my_secret', 
                host='localhost', 
                hi=None
            )
        ), 
        yet_another_config=YetAnotherConfig(
            secret=None
        ), 
        yet_another_config_list=[
            YetAnotherConfig(secret='goodbye'), 
            YetAnotherConfig(secret="h")
        ]
    )
    
    result_object = create_dataclass_object_from_dict(Config, input_dict)

    assert result_object == expected_object