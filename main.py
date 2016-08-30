import time
from datetime import datetime
from models.Config import Config
from models.BuffBot import BuffBot
from models.Channel import Channel

def main():
    while True:
        now = datetime.now()
        if (Config.is_business_hours(now) and now.minute == 0) or Config.debug:
            print "assigning! is_business_hours: " + str(Config.is_business_hours(now)) + " " + str(now)
            for data in Config.channels:
                channel = Channel(data)
                buffbot = BuffBot(channel)
                buffbot.assign_exercise()
            time.sleep(3)
        else:
            print now
            time.sleep(59)

main()