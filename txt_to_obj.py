import requests

prompt = "cat"
models = ["base40M","base300M"]
model = "base40M"
guidance_scale = 3 #3 to 10
grid_size = 16 #16 to 128; higher value = denser pixel

response = requests.post("https://anzorq-point-e-demo.hf.space/run/generate_txt2obj", json={
	"data": [
		prompt,
		model,
		guidance_scale,
		grid_size,
	]
}).json()

with open("txt_to_obj_response.txt", 'w') as f:
    f.write(str(response["data"]))
