import discord

import json
from os import path
import os


auth = json.loads(open("./auth.json", "r").read())["token"]


generatedSwitch = {}

cases = ["name1", "other", "third"]

class name1():
    def __init__(self):
        print(self.__class__.__name__)
    def otherMethod(self):
        print("do things")
class other():
    def __init__(self):
        print(self.__class__.__name__)

class third():
    def __init__(self):
        print(self.__class__.__name__)

for case in cases:
    generatedSwitch[case] = globals()[case]


potato = generatedSwitch["name1"]()

potato.otherMethod