import json
import requests
import time
from models.Config import Config

config = Config()

USER_TOKEN_STRING =  config.user_token
URL_TOKEN_STRING =  config.url_token
HASH = "%23"

class Slack:

    def __init__(self):
        self.user_queue = []
        self.first_run = True
        self.logfile = "log" + time.strftime("%Y%m%d-%H%M") + ".csv"

        self.debug = config.debug

        self.team_domain = config.team_domain
        self.channel_id = config.channel_id
        self.channel_name = config.channel_name

        self.post_URL = "https://" + self.team_domain + ".slack.com/services/hooks/slackbot?token=" + URL_TOKEN_STRING + "&channel=" + HASH + self.channel_name

    def send_message(self, message):
        # TODO
        pass

    def fetch_active_user_ids(self):
        response = requests.get("https://slack.com/api/channels.info",
            params={
                "token": USER_TOKEN_STRING,
                "channel": self.channel_id
            }
        )
        return json.loads(response.text, encoding="utf-8")["channel"]["members"]

    def fetch_user(self, id):
        response = requests.get("https://slack.com/api/users.info",
            params={
                "token": USER_TOKEN_STRING,
                "user": id
            }
        )
        return json.loads(response.text, encoding="utf-8")["user"]

    def is_user_active(self, id):
        try:
            response = requests.get("https://slack.com/api/users.getPresence",
                params={
                    "token": USER_TOKEN_STRING,
                    "user": id
                }
            )
            status = json.loads(response.text, encoding="utf-8")["presence"]
            return status == "active"
        except requests.exceptions.ConnectionError:
            print "Error fetching online status for " + self.handle
            return False