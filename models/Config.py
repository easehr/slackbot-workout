import datetime
import json
import os
import time
from dateutil import tz

CONFIG_FILE = "config.json"

class Config:

    logfile = "log" + time.strftime("%Y%m%d-%H%M") + ".csv"

    @staticmethod
    def is_business_hours(current):

        if not Config.business_hours["on"]:
            if Config.debug:
                print "not business hours"
            return True

        from_zone = tz.gettz(Config.business_hours["timezone_server"])
        to_zone = tz.gettz(Config.business_hours["timezone_local"])

        now = current.replace(tzinfo=from_zone).astimezone(to_zone).time()
        start = datetime.time(Config.business_hours["start"])
        end = datetime.time(Config.business_hours["end"])

        if start <= now and now <= end:
            if Config.debug:
                print "inside business hours"
            return True
        else:
            if Config.debug:
                print "outside business hours"
            return False

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)
    for k, v in config.items():
        setattr(Config, k, v)