import requests

# .get is a server request that sends:
    # Headers - meta data, slightly hidden e.g screen size, devic info etc.
    # Path - URL sectionr that determines where to send info, a location on the internet
    # Arguments - information you send (as is headers)

headers = ''
path = 'http://api.postcodes.io/postcodes/'
arguments = 'E146GT'

post_code_req = requests.get(path + arguments)
# print(post_code_req)
# print(post_code_req.status_code)
print(post_code_req.headers)
print(type(post_code_req.content))
print(type(post_code_req.json()))

dict_of_requests = post_code_req.json() # --> then you can use it

