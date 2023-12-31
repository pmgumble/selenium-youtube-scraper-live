import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"  
# Doesen't Execute js
response = requests.get(YOUTUBE_TRENDING_URL)

# print('Status Code', response.status_code)
# print("Output", response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title:', doc.title.text)

# Find all the video divs
# Look for all the divs with the class
video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'Found {len(video_divs)} videos')
