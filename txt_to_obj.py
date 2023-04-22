import requests

DEBUG = True

prompt = "a piano"
models = ["base40M","base300M"]
model = "base40M"
guidance_scale = 3 #3 to 10
grid_size = 128 #16 to 128; higher value = denser pixel

try:
	response = requests.post("https://anzorq-point-e-demo.hf.space/run/generate_txt2obj", json={
              "data": [
              prompt,
              model,
              guidance_scale,
              grid_size
			  ]}).json()
except:
	print("---------------------")
	print("Internal server error")
	print("---------------------")

### save file for testing ###
# with open("txt_to_obj_response.txt", 'w') as f:
#     f.write(str(response["data"]))
### end save ###

### data extraction ###
data = response["data"]
output1 = data[1]
output2 = data[2]
if DEBUG:
	##### check the things in the dictionary #####
	print("Output1:")
	[print(k,v) for k,v in output1.items()]
	print("\nOutput2:")
	[print(k,v) for k,v in output2.items()]
	##### end check #####
file_OBJ = output1["name"]
url = "https://anzorq-point-e-demo.hf.space/file=" + file_OBJ

print(f"\nRequesting to url {url}\n")
### end extraction


### request twice: first request always fail ###
try:   
    r = requests.get(url)
except:
    r = requests.get(url)
    
obj_text = r.text #decode text (only for OBJ file in this case)

# save file
with open("model.obj", "w") as f:
    f.write(obj_text)
    
