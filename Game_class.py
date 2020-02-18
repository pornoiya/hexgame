from tkinter import *
import random
import Additional_module as a_d
import Player_class as Point
import Hexagon_class as Hex
import const_file as const
import dijkstra as dj
import datetime


class Game:
    START_SESSION = datetime.datetime.now()
    DELTA_TIME = datetime.timedelta(0, 0, 0)

    @staticmethod
    def heap_of_moves(moves, color, c):
        list_of_sub_chains = []
        for mv in moves:
            sub_chains = []
            for another_mv in moves:
                if another_mv in dj.Dj.generate_neighbors(mv):
                    sub_chains.append(mv)
                    sub_chains.append(another_mv)
            if sub_chains not in list_of_sub_chains:
                list_of_sub_chains.append(sub_chains)
        for lst in list_of_sub_chains:
            for another_lst in list_of_sub_chains:
                for item in lst:
                    if lst != another_lst and item in another_lst:
                        new = lst + another_lst
                        try:
                            list_of_sub_chains.remove(another_lst)
                            list_of_sub_chains.append(list(set(new)))
                        except ValueError:
                            break
        for chain in a_d.Functions.make_unique_list(list_of_sub_chains):
            if color == const.player_one.color:
                if len(chain) >= const.GRID_SIZE:
                    if a_d.Functions.is_chain_done(chain, const.ORIENTATIONS_DICTIONARY[color]):
                        Game.winning_message(const.player_one, c)
            elif color == const.player_two.color:
                if len(chain) >= const.GRID_SIZE:
                    if a_d.Functions.is_chain_done(chain, const.ORIENTATIONS_DICTIONARY[color]):
                        Game.winning_message(const.player_two, c)

    @staticmethod
    def winning_message(player, c):
        Game.DELTA_TIME = datetime.datetime.now() - Game.START_SESSION
        c.create_text((const.START_POINT.x + const.WINDOW_WIDTH) / 2, (const.START_POINT.y + const.WINDOW_HEIGHT) / 2 + 50,
                      text=str(datetime.timedelta(seconds=Game.DELTA_TIME.seconds)), justify=CENTER, font="Verdana 28", fill="black")
        c.create_text((const.START_POINT.x + const.WINDOW_WIDTH) / 2, (const.START_POINT.y + const.WINDOW_HEIGHT) / 2,
                      text="{} won!".format(player.color), justify=CENTER, font="Verdana 28", fill="black")

    @staticmethod
    def generate_hex_map(start_point, map_size, size, color, c):
        even_delta = Point.Point(float(const.WIDTH_OF_HEX) / 2, 3 * float(size) / 2)
        for j in range(0, map_size):
            Hex.Hexagon.draw_row(Point.Point(start_point.x + j * even_delta.x, start_point.y + even_delta.y * j),
                             size, map_size, j, color, c)

    @staticmethod
    def ai_instructions(c):
        try:
            ids = c.find_withtag(CURRENT)[0]
            if ids not in const.clicked:
                c.itemconfig(CURRENT, fill=dj.Dj.player_one.color)
                const.blue_player.append(ids)
                const.clicked.add(ids)
                cells = dj.Dj.build_path(1, const.GRID_SIZE * (const.GRID_SIZE - 1) + 1)
                cell = random.choice(cells)
                while cell in const.clicked:
                    if cell in const.blue_player:
                        cell = random.choice(cells)
                        cells = dj.Dj.build_path(1, random.randint(const.GRID_SIZE * (const.GRID_SIZE - 1),
                                                             const.GRID_SIZE ** 2))
                    else:
                        cell = random.choice(cells)
                if cell not in const.blue_player:
                    c.itemconfig(cell, fill=const.player_two.color)
                    const.red_player.append(cell)
                const.clicked.add(cell)
        except IndexError:
            c.update()

    @staticmethod
    def two_players_instruction(c):
        try:
            ids = c.find_withtag(CURRENT)[0]
            if ids not in const.clicked:
                if len(const.clicked) % 2 == 0:
                    c.itemconfig(CURRENT, fill=const.player_one.color)
                    const.blue_player.append(ids)
                else:
                    c.itemconfig(CURRENT, fill=const.player_two.color)
                    const.red_player.append(ids)
                const.clicked.add(ids)
        except IndexError:
            c.update()

    @staticmethod
    def dumb_computer_instructions(c):
        try:
            ids = c.find_withtag(CURRENT)[0]
            if ids not in const.clicked:
                c.itemconfig(CURRENT, fill=const.player_one.color)
                const.blue_player.append(ids)
                const.clicked.add(ids)
                cell = random.randint(1, const.GRID_SIZE ** 2)
                if const.GRID_SIZE ** 2 - len(const.clicked) > 1:
                    while cell in const.clicked:
                        cell = random.randint(1, const.GRID_SIZE ** 2)
                if cell not in const.blue_player:
                    c.itemconfig(cell, fill=const.player_two.color)
                    const.red_player.append(cell)
                const.clicked.add(cell)
        except IndexError:
            c.update()

    @staticmethod
    def click(event, c):
        if const.args['regime'] == "dumb":
            Game.dumb_computer_instructions(c)
        elif const.args['regime'] == "two":
            Game.two_players_instruction(c)
        elif const.args['regime'] == "ai":
            Game.ai_instructions(c)
        Game.heap_of_moves(const.blue_player, const.player_one.color, c)
        Game.heap_of_moves(const.red_player, const.player_two.color, c)

