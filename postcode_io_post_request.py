import json
import requests

# POST requests have eberything a GET request had PLUS json or XML
    # We'll cover json

headers = {'Content-Type': 'application/json'}
path = 'http://api.postcodes.io/postcodes/'
arguments = ''

json_body = json.dumps({"postcodes": ["E14 6GT", "TN27 9NF", "NE30 1DF"]})

multi_post_codes = requests.post(path, headers = headers, data = json_body)

dict_multi_results= multi_post_codes.json()['result']

print(dict_multi_results)