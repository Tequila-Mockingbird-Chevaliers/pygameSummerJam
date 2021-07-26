import src.constants as const


class BrickGenerator:
    """
    BrickGenerator class
    """

    def __init__(self, level: int):
        """
        Initialise BrickGenerator
        """
        self.bricks: list[tuple[int, int]] = []
        self.load_level(level)

    def load_level(self, level: int):
        """
        Load a level
        """
        level_file = const.LEVELS_FOLDER / f"level{level}.txt"
        text = [x.strip() for x in level_file.read_text().splitlines()]

        for row, row_contents in enumerate(text):
            for col, char in enumerate(row_contents):
                if char == "x":
                    self.bricks.append((col, row))
