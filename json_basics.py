import json

car_data = {
    'engine': 'electric',
    'brand': 'Peugeot',
    'price': 13000,
    'model': 'Ze',
}
print(type(car_data))

# dict -> str using json.dumps(dict)
car_data_json_string = json.dumps(car_data)

print(car_data_json_string) # Not a dictionary, even though it looks like one. You can't index it
# in the same way '9' is not an integer, but a string. It looks like a number but can't act like one
print(type(car_data_json_string))

# Write a json file
car_data = {
    'engine': 'electric',
    'brand': 'Peugeot',
    'price': 13000,
    'model': 'Ze',
}

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile)
    # json.dump(arg1, arg2) --> .json file
        # arg1 = dictionary
        # arg2 = file to dump the json into (it will create it if it doesn't already exist)