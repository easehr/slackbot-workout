import requests
from models.Config import Config
from models.Slack import Slack

class User:

    def __init__(self, user_id):
        self.id = user_id
        self.user = Slack.fetch_user(self.id)
        self.username = self.user["name"]
        self.realname = self.user["profile"]["real_name"]
        self.handle = ("@" + self.username).encode("utf-8")

    def is_active(self):
        return Slack.is_user_active(self.id)