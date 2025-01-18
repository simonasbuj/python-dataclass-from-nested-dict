from dataclasses import dataclass

@dataclass
class Config:
    base_path: str
    path: str



if __name__ == "__main__":

    default_value = {"base_path": "my-path", "path": "my/full/path/default.csv"}
    cli_value = {"base_path": "my-overriden-path"}
    
    # override default dict with values from cli
    config_dict = {**default_value, **cli_value}

    config = Config(**config_dict)
 

    print(config)
    print(config.base_path)