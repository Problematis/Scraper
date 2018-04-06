import requests

response_object = requests.get('http://edmundmartin.com')
print(response_object.text)
