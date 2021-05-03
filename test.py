import requests

BASE="http://127.0.0.1:5000/"

data=[{"likes":10, "name":"Joe1", "views":300},
		{"likes":10, "name":"Resting", "views":15000},
		{"likes":10, "name":"Tim", "views":7500},
		{"likes":10, "name":"Bnag", "views":9800}]

for i in range(len(data)):
	response=requests.put(BASE + "video/"+ str(i), data[i])
	print(response.json())

input()
response=requests.get(BASE + "video/6")
print(response.json())