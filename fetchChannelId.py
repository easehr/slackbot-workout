'''
A quick script to fetch the id of a channel you want to use.

USAGE: python fetchChannelId.py <channel_name>
'''

import requests
import sys
import os
import json

USER_TOKEN_STRING = "xoxp-2698058516-4419142126-18791187975-cc67c78927"
URL_TOKEN_STRING = "T1VaUJujb2hsUGeGPtWjtvTo"
HASH = "%23"

channelName = sys.argv[1]
response = requests.get("https://slack.com/api/channels.list", params={"token": USER_TOKEN_STRING })
channels = json.loads(response.text, encoding="utf-8")["channels"]

for channel in channels:
    if channel["name"] == channelName:
        print channel["id"]
        break