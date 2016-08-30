import json
import requests
from models.Config import Config

HASH = "%23"

class Slack:

    TEAM_DOMAIN = Config.team_domain
    USER_TOKEN =  Config.user_token
    URL_TOKEN =  Config.url_token
    BASE_URL = "https://slack.com/api/"

    @staticmethod
    def fetch_active_user_ids(channel_id):
        response = Slack._fetch("channels.info",
            params={
                "token": Slack.USER_TOKEN,
                "channel": channel_id
            }
        )
        return response["channel"]["members"]

    @staticmethod
    def fetch_user(user_id):
        response = Slack._fetch("users.info",
            params={
                "token": Slack.USER_TOKEN,
                "user": user_id
            }
        )
        return response["user"]

    @staticmethod
    def is_user_active(user_id):
        response = Slack._fetch("users.getPresence",
            params={
                "token": Slack.USER_TOKEN,
                "user": user_id
            }
        )
        status = response["presence"]
        return status == "active"

    @staticmethod
    def send_message(channel, message):
        response = requests.post(channel.url,
            data=json.dumps({
                "text": message
            })
        )
        print response.text

    @staticmethod
    def _fetch(endpoint, params):
        try:
            response = requests.get(Slack.BASE_URL + endpoint, params=params)
            return json.loads(response.text, encoding="utf-8")
        except Exception, e:
            print "*** ERROR *** Error fetching " + endpoint + ": " + str(e)