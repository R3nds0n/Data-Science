import requests
import re

url = "https://www.google.com/"
r = requests.get(url)
text = r.text

re.search('.png', text, re.IGNORECASE)

print(text)