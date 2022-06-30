### config parser

from configparser import ConfigParser

config = ConfigParser()

config["MEDIUM"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Player"
}

config["HARD"] = {
    "numberdigits": 10,
    "numbertries": 6,
    "playername": "Pie"
}

config["EASY"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Cheater",
    "cheats": "on"
}

with open("number_guessing.ini", "w") as f:
    config.write(f)














#
