import json
import requests
import os
from config import api_key

keyword = "ironman"
page = ""
folder = "3D_model_finder/STLfiles"
image_folder = "3D_model_finder/Images"

front_link = "https://api.thingiverse.com/"
auth_link = f"?access_token={api_key}"

if not os.path.exists(folder):
    os.makedirs(folder)
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

def generate_url(action, keyword, page):
    if action == "search":
        prefix = "search/"
        suffix = ""
    elif action == "get files":
        prefix = "things/"
        suffix = "/files"

    keyword_link = f"{keyword}"

    if not page: page = 1 #default 1
    page_link = f"&page={page}"

    full_link = front_link + prefix + keyword_link + suffix + auth_link + page_link

    print(f"accessing {full_link}")

    return full_link

def fetch_data(url):
    response = requests.get(url)
    data = json.loads(response.text)

    return data

def data_reader(data):
    for hit in data['hits']:
        print(f"Result ID: {hit['id']}")
        print(f"Name: {hit['name']}")
        print(f"URL: {hit['public_url']}")
        print(f"Created at: {hit['created_at']}")
        print(f"Thumbnail URL: {hit['thumbnail']}")
        print(f"Preview image URL: {hit['preview_image']}")
        print(f"Comment count: {hit['comment_count']}")
        print(f"Make count: {hit['make_count']}")
        print(f"Like count: {hit['like_count']}")
        print("Tags:")
        for tag in hit['tags']:
            print(f"\t{tag['name']}: {tag['count']}")
        print("\n")

def data_converter(data):
    result = []
    for hit in data['hits']:
        dict_holder = {}
        dict_holder['id'] = hit['id']
        dict_holder['name'] = hit['name'].replace(" ", "_").replace("/", "-").replace(":", "-")
        dict_holder['preview_image'] = hit['preview_image']
        result.append(dict_holder)

    return result

def multiple_files_indicator(result):
    s = requests.Session()
    for thing in result:
        id = thing["id"]
        url = generate_url(action="get files", keyword=id, page=1)
        response = s.get(url)
        data = response.json()
        file_num = len(data)
        print(f"{thing['name']} has {file_num} parts")

def download_file(result, choice=1):
    index = choice - 1
    thing = result[index]
    id = thing["id"]
    thing_name = thing["name"]
    thing_data = fetch_data(generate_url(action="get files", keyword=id, page=1))

    print(f"Downloading {thing_name} files")

    s = requests.Session()

    if not os.path.exists(f"{folder}/{thing_name}"):
        os.makedirs(f"{folder}/{thing_name}")

    for file in thing_data:
        file_name = file['name']
        if file_name.endswith('.STL') or file_name.endswith('.OBJ') or file_name.endswith('.stl') or file_name.endswith('.obj'):
            url = file['download_url']+auth_link
            file_path = f"{folder}/{thing_name}/{file_name}"
            
            response = s.get(url)
            with open(file_path,"wb") as f:
                f.write(response.content)
            print(f"Model Saved Successfully: {file_name} ----> {folder}/{thing_name}")

def download_images(result):
    s = requests.Session()
    for thing in result:
        thing_name = thing["name"]
        thing_img_url = thing["preview_image"]
        file_path = f"{image_folder}/{thing_name}.jpg"
        response = s.get(thing_img_url)
        with open(file_path,"wb") as f:
            f.write(response.content)
        print(f"Preview Image Saved Successfully: {file_path}")

if __name__ == "__main__":
    data = fetch_data(generate_url(action="search", keyword=keyword, page=page))

    result = data_converter(data)

    # multiple_files_indicator(result)

    # download_images(result)

    download_file(result, 5)
    


    