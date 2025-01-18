
if __name__ == "__main__":

    default_value = {
        "bucket": "my-bucket", 
        "path": "my/full/path/default.csv",
        "nest": {
            "key_01": "value_01"
        }
    }
    cli_value = {
        "bucket": "overwritten_bucket",
        "nest": {
            "key_01": "value_03"
        }
    }
    
    # override default dict with values from cli
    config_dict = {**default_value, **cli_value}

    print(config_dict)