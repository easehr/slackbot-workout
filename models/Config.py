import os
import json
import datetime
from dateutil import tz

CONFIG_FILE = "config.json"

class Config:

    def __init__(self):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            for k, v in config.items():
                setattr(self, k, v)

    def get_exercise(self, id):
        for exercise in self.exercises:
            if exercise["id"] == id:
                return exercise

    def is_business_hours(self):
        if not self.business_hours["on"]:
            if self.debug:
                print "not business hours"
            return True
        from_zone = tz.gettz(self.business_hours["timezone_server"])
        to_zone = tz.gettz(self.business_hours["timezone_local"])
        now = datetime.datetime.now().replace(tzinfo=from_zone).astimezone(to_zone).time()
        start = datetime.time(self.business_hours["start"])
        end = datetime.time(self.business_hours["end"])
        if start <= now and now <= end:
            if self.debug:
                print "inside business hours"
            return True
        else:
            if self.debug:
                print "outside business hours"
            return False