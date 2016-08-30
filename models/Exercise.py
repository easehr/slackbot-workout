import random
from models.Config import Config

config = Config()

class Exercise:

    def __init__(self, id):
        self.id = id
        values = config.get_exercise(self.id)
        self.name = values["name"]
        self.quantities = values["quantities"]
        self.unit = values["unit"]

    def get_set(self):
        idx = random.randrange(0, len(self.quantities))
        return str(self.quantities[idx]) + " " + self.unit + "s " + self.name