import argparse
import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    secret: str
    something_else: str
    must_have: bool
    missing: Optional[str] = None
    


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Parse config JSON from command line")

    # Add the --config argument
    parser.add_argument('--config', type=str, required=True, help='Configuration in JSON format')

    # Parse the arguments
    args = parser.parse_args()

    # Load the JSON string into a Python dictionary
    config_dict = json.loads(args.config)
    config = Config(**config_dict)
    print(config)

if __name__ == "__main__":
    main()
