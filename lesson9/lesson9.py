import urllib.request
import requests

opener = urllib.request.build_opener()
response = opener.open("http://www.google.com")
print(response.read())

response = requests.get("http://www.google.com")
# print(response.text)
print(response.content)
print("Type", type(response.content))
print("Type", type(response.text))


response = requests.post("http://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
print(response.text)



