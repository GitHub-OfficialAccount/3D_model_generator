from gradio_client import Client
import random

prompt_hidden = "front view, full view, outer view, third person perspective, complete body fully visible, whole structure clearly exposed, detailed, intricate, simplistic, trending on artstation, 4 k, hyperrealistic, 5 mm, focused, extreme details, unreal engine 5, masterpiece"
negative_prompt_hidden = "poor quality, blurry, worst quality, bad quality, uncovered, obscene, horror, low resolution"

prompt = "hamburger"
negative_prompt = ""
height = "512"
width = "512"
seed = 13 #random.randint(0,100000) #each seed shows a different result
num_step = 41
cfg_weight = 10
color_weight_lamda = 1
parameter_5 = "" #I dont know what this is

full_prompt = prompt + ", " + prompt_hidden
if negative_prompt:
    full_negative_prompt = negative_prompt + ", " + negative_prompt_hidden
else:
    full_negative_prompt = negative_prompt_hidden

print(f"\nfull_prompt: {full_prompt}\n")
print(f"full_negative_prompt: {full_negative_prompt}\n")

client = Client("https://songweig-rich-text-to-image.hf.space/")
result = client.predict(
				{"ops": [{"insert": f"{full_prompt}"}]},	# str representing string value in 'Rich-text JSON Input' Textbox component
				full_negative_prompt,	# str representing string value in 'Negative Prompt' Textbox component
				height,	# str representing Option from: [512] in 'height' Dropdown component
				width,	# str representing Option from: [512] in 'Width' Dropdown component
				seed,	# int | float representing numeric value between 0 and 100000 in 'Seed' Slider component
				num_step,	# int | float representing numeric value between 0 and 100 in 'Number of Steps' Slider component
				cfg_weight,	# int | float representing numeric value between 0 and 50 in 'CFG weight' Slider component
				color_weight_lamda,	# int | float representing numeric value between 0 and 2 in 'Color weight lambda' Slider component
				parameter_5,	# str representing string value in 'parameter_5' Textbox component
				fn_index=4
)

# result = client.predict(
# 				"Howdy!",	# str representing string value in 'Font size examples' Dataset component
# 				fn_index=3
# )
print(result)
