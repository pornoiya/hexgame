import const_file as const
import Player_class as Player_Point
import math


class Hexagon(object):
    def __init__(self, start_point, size, color, c=None, hide=True):
        self.points = Hexagon.generate_hex_points_list(start_point, size)
        self.color = color
        if hide:
            self.instance = c.create_polygon(self.points[0].x, self.points[0].y, self.points[1].x, self.points[1].y,
                                             self.points[2].x, self.points[2].y, self.points[3].x, self.points[3].y,
                                             self.points[4].x, self.points[4].y, self.points[5].x, self.points[5].y,
                                             fill=self.color, outline="black")
        self.centre = Player_Point.Point(self.points[2].x + const.WIDTH_OF_HEX / 2, self.points[2].y + size / 2)

    @staticmethod
    def hex_corner(start_point, size, i):
        angle_deg = 60 * i + 30
        angle_rad = float(math.pi) / 180 * angle_deg
        return Player_Point.Point(start_point.x + size * math.cos(angle_rad), start_point.y + size * math.sin(angle_rad))

    @staticmethod
    def generate_hex_points_list(start_point, size):
        points = []
        for j in range(1, 7):
            corner_coordinates = Hexagon.hex_corner(start_point, size, j)
            points.append(corner_coordinates)
        return points

    @staticmethod
    def draw_row(start_point, size, count_hex, j, color, c):
        for i in range(0, count_hex):
            Hexagon(start_point, size, color, c)
            start_point.x = start_point.x + const.WIDTH_OF_HEX
