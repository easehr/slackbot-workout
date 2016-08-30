import time
from datetime import datetime
from models.Config import Config
from models.BuffBot import BuffBot

config = Config()
buffbot = BuffBot()

def main():
    while True:
        now = datetime.now()
        if (config.is_business_hours and now.minute == 0) or config.debug:
            print "assigning! is_business_hours: " + str(config.is_business_hours()) + " " + str(now)
            buffbot.assign_exercise()
            time.sleep(5)
        else:
            print now
            time.sleep(60)

main()