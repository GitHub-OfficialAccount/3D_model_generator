from gradio_client import Client

client = Client("https://eccv2022-dis-background-removal.hf.space/")
result = client.predict(
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str representing filepath or URL to image in 'image' Image component
				api_name="/predict"
)
print(result)