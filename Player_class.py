import const_file as c


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Player:
    def __init__(self, color):
        self.color = color
        self.orientation = c.ORIENTATIONS_DICTIONARY[color]

