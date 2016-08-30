import random
from models.Config import Config

class Exercise:

    def __init__(self, data):
        self.quantities = data["quantities"]
        self.name = data["name"]
        self.unit = data["unit"]

    @staticmethod
    def get_random():
        idx = random.randrange(0, len(Config.exercises))
        exercise = Exercise(Config.exercises[idx])
        return exercise

    def get_set(self):
        idx = random.randrange(0, len(self.quantities))
        quantity = self.quantities[idx]
        name = self.name
        unit = self.unit
        return str(quantity) + " " + unit + "s " + name

