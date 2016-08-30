import random
from models.Config import Config
from models.Slack import Slack
from models.User import User
from models.Exercise import Exercise

config = Config()

class BuffBot:

    def __init__(self):
        self.slack = Slack()
        self.exercises = config.exercises

    def select_users(self):
        selected_users = []
        selected_ids = []
        active_user_ids = self.slack.fetch_active_user_ids()
        for x in range(config.num_people):
            idx = random.randrange(0, len(active_user_ids))
            user_id = active_user_ids[idx]
            if user_id not in selected_ids:
                selected_ids.append(user_id)
        for id in selected_ids:
            user = User(id)
            if user.is_active:
                selected_users.append(user)
        return selected_users

    def select_exercise(self):
        idx = random.randrange(0, len(self.exercises))
        return Exercise(self.exercises[idx]["id"])

    def assign_exercise(self):
        exercise = self.select_exercise()
        announcement = exercise.get_set() + " "

        if random.random() < config.group_callout_chance:
            announcement += "@channel!"
        else:
            users = self.select_users()
            handles = [user.handle for user in users]
            for i, handle in enumerate(handles):
                announcement += handle
                if i < len(handles) - 1:
                     announcement += " and "
            announcement += "!"


        if not config.debug:
            self.slack.send_message(announcement)
        print announcement