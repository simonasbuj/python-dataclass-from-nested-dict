import argparse
import yaml
import sys

def main(yaml_content):
    # Load the YAML configuration from the string
    try:
        config = yaml.safe_load(yaml_content)
        print(config)  # Print the loaded configuration
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Load configuration from YAML content.')
    parser.add_argument('--my-yaml', type=str, required=True, help='YAML configuration as a string')

    args = parser.parse_args()

    # Call the main function with the provided YAML content
    main(args.my_yaml)
