"""
data to collect = > 
Video title,
description, 
publishing datetime, 
thumbnails URLs 
"""


import argparse
from re import A

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import requests
import asyncio


DEVELOPER_KEY = 'AIzaSyBWcRihO22qv51qtMR2SqkK7aLGkKxtpU0'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)


  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
                                    q=options["query"],
                                    part='id,snippet',
                                    maxResults= 10).execute()
  
  videos_name = []
  description = []
  publishing_date = []
  videos_id = []
  channels = []
  thumbnail_url = []

  for search_result in search_response.get('items', []):
    if search_result['snippet']:
        videos_name.append('%s ' % (search_result['snippet']['title']))
        description.append('%s ' % (search_result['snippet']['description']))
        publishing_date.append('%s ' % (search_result['snippet']['publishedAt']))
        thumbnail_url.append('%s ' % (search_result['snippet']['thumbnails']['default']['url']))
        channels.append('%s ' % (search_result['snippet']['channelTitle']))
      

  data = {"videos_name":videos_name,"description":description,"channels":channels,"publishing_date":publishing_date,"thumbnail_url":thumbnail_url}
  
  return data

def get_video_information(options):
    """[Collect youtube video information]

    Args:
        options ([dict]): [query to search for]

    Returns:
        [dict]: [dictionary of video name,description,publishing_date,thumbnail_url]
    """
    search_results = youtube_search(options)
    return search_results