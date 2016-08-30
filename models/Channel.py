from models.Config import Config
from models.Slack import Slack
from models.User import User

class Channel:

    def __init__(self, channel):
        self.id = channel["id"]
        self.name = channel["name"]
        self.users = self.fetch_active_users()

    def fetch_active_users(self):
        ids = Slack.fetch_active_user_ids(self.id)
        users = [User(id) for id in ids]
        return users