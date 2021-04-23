import requests
from bs4 import BeautifulSoup
print("test")

URL = "https://dojo.code.ninja/students/cn-wa-newcastle/#"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="status-bar-container")

print(results.prettify())