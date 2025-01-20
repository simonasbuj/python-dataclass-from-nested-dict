from pydantic import BaseModel
from typing import List

# Define a nested Pydantic model for Address
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# Define the main Pydantic model with a list of Address
class Person(BaseModel):
    name: str
    age: int
    email: str
    addresses: List[Address]  # List of nested Address models
    friends: List[str]  # List of friends' names

# Example nested dictionary with a list of Addresses
person_dict = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "addresses": [
        {
            "street": "123 Main St",
            "city": "Anytown",
            "zip_code": "12345"
        },
        {
            "street": "456 Side St",
            "city": "Othertown",
            "zip_code": "67890"
        }
    ],
    "friends": ["Jane", "Bob", "Alice"]
}

# Create the Pydantic model object from the nested dictionary
person = Person(**person_dict)

# Print the Pydantic model object
print(person)
print(person.model_dump_json())
