# from bs4 import BeautifulSoup
# import requests

url = "https://www.thingiverse.com/search?q=ironman&type=things&sort=relevant&page=1"

# r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html.parser')
# inspected_code = str(soup.prettify())

# print(inspected_code)

# with open("temp.txt", 'w') as f:
#     f.write(inspected_code)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create Chrome options and set to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")

# Create a new instance of the Chrome driver with headless mode options
driver = webdriver.Chrome(options=chrome_options)

# Load cookies from file
driver.get(url)
cookies = driver.get_cookies()
cookie_file = "cookies.txt"
with open(cookie_file, "w") as f:
    for cookie in cookies:
        f.write(f"{cookie['name']}={cookie['value']}; path={cookie['path']}; domain={cookie['domain']}\n")

# Create a new instance of the Chrome driver with headless mode options and cookies
driver.quit()
chrome_options.add_argument(f"--user-data-dir={cookie_file}")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
driver.get(url)

# Get the final HTML code after executing any JavaScript on the page
final_html_code = driver.page_source

# Close the browser
driver.quit()

with open('temp.txt', 'w', encoding='utf-8') as f:
    f.write(final_html_code)