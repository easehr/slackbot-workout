import random
from models.Config import Config
from models.Slack import Slack
from models.User import User
from models.Exercise import Exercise

# One BuffBot for each channel
class BuffBot:

    def __init__(self, channel):
        self.channel = channel
        self.exercises = Config.exercises

    def select_users(self):
        users = []
        for i in range(Config.num_people):
            idx = random.randrange(0, len(self.channel.users))
            user = self.channel.users[idx]
            users.append(user)
        return users

    def get_announcement(self, users, exercise):
        announcement = exercise.get_set() + " "
        if random.random() < Config.group_callout_chance:
            announcement += "@channel!"
        else:
            handles = [user.handle for user in users]
            for i, handle in enumerate(handles):
                announcement += handle
                if i < len(handles) - 1:
                    announcement += " and "
            announcement += "!"

        return announcement

    def assign_exercise(self):
        users = self.select_users()
        exercise = Exercise.get_random()
        announcement = self.get_announcement(users, exercise)
        if not Config.debug:
            Slack.send_message(self.channel, announcement)
        print announcement