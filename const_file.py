import math
import Player_class as pc

REGIMES = ['ai', 'dumb', 'two']
args = {'size': 7, 'regime': 'dumb'}

GRID_SIZE = args['size']
HEX_SIZE = 30
WIDTH_OF_HEX = math.sqrt(3) * HEX_SIZE
HEIGHT_OF_HEX = 2 * HEX_SIZE
START_POINT = pc.Point(80, 50)
WINDOW_HEIGHT = (WIDTH_OF_HEX + START_POINT.y / 10)* GRID_SIZE
WINDOW_WIDTH = (HEIGHT_OF_HEX + START_POINT.x / 2) * GRID_SIZE
MAP_COLOR = "white"
ORIENTATIONS_DICTIONARY = {"blue": "horisontal", "red": "vertical"}
player_one = pc.Player("blue")
player_two = pc.Player("red")
red_player = []
blue_player = []
clicked = set()
d = {}
visited = list(clicked)
cell_beg = 1
mark = {}


def update_size(size):
    global GRID_SIZE
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    GRID_SIZE = size
    WINDOW_HEIGHT = (WIDTH_OF_HEX + START_POINT.y / 10) * GRID_SIZE
    WINDOW_WIDTH = (HEIGHT_OF_HEX + START_POINT.x / 2) * GRID_SIZE

