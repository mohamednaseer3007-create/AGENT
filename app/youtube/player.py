import re
import urllib.parse
import urllib.request 

def get_vid(query):
  try:
    encoded = urllib.parse.quote(query)

  url = (
          "https://www.youtube.com/results"
          "?search_query=" + encoded 
  )
  request = urllib.request.Request(
      url,
      headers={
            "User-Agent": "Mozilla/5.0"
      }
  )
  data = urllib.request.urlopen(
    request,
    timeout=5
  ).read().decode("utf-8",errors="ignore")

ids = re.findall(
  r'"videoId":"([^"]+)"',
  data
)
  
