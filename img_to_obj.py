import requests

response = requests.post("https://anzorq-point-e-demo.hf.space/run/generate_img2obj", json={
	"data": [
		"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg==",
		"base40M",
		3,
		32,
	]
}).json()

data = response["data"]