import json

# Create a Python dictionary
student = {
    "name": "S Vipula",
    "register_number": "24BECS184",
    "course": "BECS",
    "marks": 85
}

# Convert dictionary into JSON string
json_string = json.dumps(student)

print("JSON String:")
print(json_string)

# Convert JSON string back into Python dictionary
python_dictionary = json.loads(json_string)

print("\nPython Dictionary:")
print(python_dictionary)