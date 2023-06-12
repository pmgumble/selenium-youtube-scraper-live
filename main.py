import smtplib
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import pandas as pd

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos


def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text

  views = video.find_element(By.CLASS_NAME, 'inline-metadata-item').text

  description = video.find_element(By.ID, 'description-text').text

  return {
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel': channel_name,
    'description': description,
    'views': views
  }


def send_email(body):

  try:
    # server = smtblib.SMTP('smtp.gmail.com',587)
    # server.ehlo()
    # server.starttls()
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()

    SENDER_EMAIL = 'pmgumble@sipnaengg.ac.in'
    RECIVER_EMAIL = 'pratikmgumble@gmail.com'
    # SENDER_PASSWORD = os.environ['GMAIL_PASSWORD']
    my_secret = os.environ['GMAIL_PASSWORD']
    # sent_from = SENDER_EMAIL
    # to = [RECIVER_EMAIL]
    subject = 'YouTube Trending Videos'

    email_text = f"""
    From: {SENDER_EMAIL}
    To: {RECIVER_EMAIL}
    Subject: {subject}
    
    {body}
    """

    server_ssl.login(SENDER_EMAIL, my_secret)
    server_ssl.sendmail(SENDER_EMAIL, RECIVER_EMAIL, email_text)
    server_ssl.close()

  except Exception as e:
    print('Something went wrong...', str(e))


if __name__ == "__main__":
  print('Creating Driver')
  driver = get_driver()

  print('Featching trending videos')
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')

  print("parsing top 10 videos")
  videos_data = [parse_video(video) for video in videos[:10]]

  print('Save the data to CSV')
  # videos_df = pd.DataFrame(videos_data)
  # print(videos_df)
  # videos_df.to_csv('trending.csv', index=None)

  print("Send an results over Email")
  body = json.dumps(videos_data, indent=2)
  send_email(body)

  print('Finished.')
