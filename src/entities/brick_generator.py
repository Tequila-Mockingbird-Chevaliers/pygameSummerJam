import os

import src.constants as const


class BrickGenerator:
    def __init__(self, level):
        self.bricks = []
        self.load_level(level)

    def load_level(self, level):
        with open(os.path.join(const.FOLDER, f"levels\\level{level}.txt")) as file:
            text = [x.strip() for x in file.readlines()]
        for row in range(len(text)):
            for column in range(len(text[row])):
                if text[row][column] == "x":
                    self.bricks.append((row, column))
