import requests

response = requests.post("https://anzorq-point-e-demo.hf.space/run/generate_txt2obj", json={
	"data": [
		"hello world",
		"base40M",
		3,
		32,
	]
}).json()

data = response["data"]

print(data)