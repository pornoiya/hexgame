#!/usr/bin/env python
import argparse
from tkinter import *
import const_file as const
import Game_class as gmain
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget
import records_data as rd
import table_records as table

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = table.UserName()
    parser = argparse.ArgumentParser(description="John Nash considered 11x11 map as the best size. "
                                                 "Enter the map size and regime: ai/two/dumb")
    parser.add_argument('-s', '--size', type=int, help='size of hex_map', default=7)
    parser.add_argument('-r', '--regime', type=str, help='game regime '
                                                         '-ai is artificial intelligence regime '
                                                         '-two is two players regime '
                                                         '-dumb is dumb computer regime', choices=const.REGIMES,
                        default='dumb')
    args = parser.parse_args().__dict__
    const.update_size(args['size'])
    root = Tk()
    root.title("HEX GAME")
    c = Canvas(root, width=const.WINDOW_WIDTH, height=const.WINDOW_HEIGHT, bg="#334433")
    c.pack()
    gmain.Game.generate_hex_map(const.START_POINT, const.GRID_SIZE, const.HEX_SIZE, const.MAP_COLOR, c)
    c.bind("<Button-1>", lambda event: gmain.Game.click(event, c))
    root.mainloop()
    with open('records.txt', 'a') as f:
        f.write(user.line_edit.text() + ' ' + str(gmain.Game.DELTA_TIME.seconds) + '\n')
        db = rd.DataBase()
        db.format_data("records.txt")
    tw = QTableWidget()
    table.Table.fill_table(tw)
    sys.exit(app.exec_())
