# install dependencies
from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.google.com/").text
soup = BeautifulSoup(html, "html5lib")

first_paragraph = soup.find("p")

print(first_paragraph)