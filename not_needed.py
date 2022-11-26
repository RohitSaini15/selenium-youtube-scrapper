import requests  # get the data present on the web page into simple response
from bs4 import BeautifulSoup  # for parsing the html document

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

#does not execute the javascript so only get the simple html page
response = requests.get(YOUTUBE_TRENDING_URL)

with open("youtube_trending.html", "w") as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, "html.parser")

print(doc.title)
