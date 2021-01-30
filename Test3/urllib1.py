import math
import urllib.request
#
# response=urllib.request.urlopen('http://www.baidu.com')
# print(response.status)
# # print(response.read())
# print(response.headers)

# print(math.ceil(5.5))
# print(math.floor(3.6))
# print(math.sqrt(74))
import requests
pyload={"水果":"苹果"}
r=requests.get('http://httpbin.org/get',params=pyload)
# print(r.encoding)
# print(r.text)
print(r.url)
print(r.status_code)
print(r.json)
