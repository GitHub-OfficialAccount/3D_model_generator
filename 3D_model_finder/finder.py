import json
import requests
import os
from config import api_key

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

def data_converter(data): #clean data
    result = []
    for hit in data['hits']:
        dict_holder = {}
        dict_holder['id'] = hit['id']
        dict_holder['name'] = hit['name'].replace(" ", "_").replace("/", "-").replace(":", "-").replace('"', "-").replace("(","-").replace(")","-")
        dict_holder['preview_image'] = hit['preview_image']
        result.append(dict_holder)

    return result

def multiple_files_indicator(result): #indicates whether the number of parts a 3D model has
    s = requests.Session()
    for i in range(len(result)):
        thing = result[i]
        id = thing["id"]
        url = generate_url(action="get files", keyword=id, page=1)
        response = s.get(url)
        data = response.json()
        file_num = len(data)
        result[i]["parts"] = file_num
        # print(f"{thing['name']} has {file_num} parts")
    return result

def download_file_from_index(result, index=0):
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

def get_image_url_from_index(result, index):
    name = result[index]['name']
    img_url = f"3D_model_finder/Images/{name}.jpg"
    return img_url

if __name__ == "__main__":
    keyword = "ironman"
    page = ""
    
    data = fetch_data(generate_url(action="search", keyword=keyword, page=page)) 
    result = data_converter(data) #clean data
    result = multiple_files_indicator(result) #indicates whether the number of parts a 3D model has

    download_images(result)

    # choice = 5 #user input

    # download_file_from_choice(result, choice)

    # img_url = get_image_url_from_choice(result, choice)
    
    # print(img_url)

    