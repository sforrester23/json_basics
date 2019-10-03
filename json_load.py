import json
# Here we load/decode json

with open('new_json_file.json', 'r') as jsonfile:
    # convert to a dictionary
    car_dictionary = json.load(jsonfile)
    print(type(car_dictionary))
    print(car_dictionary['brand'], car_dictionary['model'], '\nSteal this baby for only', car_dictionary['price'])