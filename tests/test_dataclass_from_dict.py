from nested_dataclass_from_dict import create_dataclass_object_from_dict
from nested_dataclass_from_dict import Config

def test_create_dataclass_object_from():
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
            "secrets": "goodbye"
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