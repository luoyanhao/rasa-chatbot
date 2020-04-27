import random


class Template():
    def __init__(self):
        self.sentence = []


    def getRandom(self, params):
        index = random.Random.randint(0,len(self.sentence))
        return self.sentence[index]