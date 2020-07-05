# 18. Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

# print(help(json))

dict_data = {"name": "Prajwol", "age": 23}

print(dict_data)
print(type(dict_data))

serialized = json.dumps(dict_data)

print(f"Serialized: {serialized}")
print(type(serialized))

deserialized = json.loads(serialized)


print(f"Deserialized: {deserialized}")
print(type(deserialized))
