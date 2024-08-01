import requests as req, json
from bs4 import BeautifulSoup as bs

url = "https://www.bu.edu/president/boston-university-facts-stats/"
response = req.get(url)
print(response.status_code)
content = response.content
content = bs(content, "html.parser")
print(type(content.body))

with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D22REF_json.json", "w") as p:
    json.dump(content.body.get_text(), p, ensure_ascii=False, indent=4)