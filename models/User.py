import requests
from models.Config import Config
from models.Slack import Slack

config = Config()
slack = Slack()

class User:

    def __init__(self, user_id):
        self.id = user_id
        self.user = slack.fetch_user(self.id)
        self.username = self.user["name"]
        self.realname = self.user["profile"]["real_name"]
        self.handle = ("@" + self.username).encode('utf-8')
        print "New user: " + self.realname + " (" + self.username + ")"

    def is_active(self):
        return slack.is_user_active(self.id)