import requests
from bs4 import BeautifulSoup # used for HTML web scraping


url = "https://www.cs.columbia.edu/~hgs/audio/harvard.html"
response = requests.get(url) # pull info from site
print(response.status_code) # print the status of said website (200 is success)
content = response.content # pulls all content from site
parsed = BeautifulSoup(content, "html.parser") # BS parses content
print(parsed.title.get_text())
print(parsed.body.get_text())