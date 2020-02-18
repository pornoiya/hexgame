#!/usr/bin/env python
import unittest
import math
import Additional_module as a_d
import const_file
from records_data import DataBase
import collections
from dijkstra import Dj
import Hexagon_class as hex_class
from Player_class import Point


class TestDijkstraModule(unittest.TestCase):
    def test_sm(self):
        p = Point(2, 4)
        self.assertTupleEqual((p.x, p.y), (2, 4))

    def test_generate_two_neighs(self):
        neighs = Dj.generate_neighbors(1, 7)
        self.assertEqual(neighs, {2, 8})
    
    def test_dijkstra_function_simple_line(self):
        path_act = Dj.build_path(1, 7)
        self.assertListEqual(path_act, [7, 6, 5, 4, 3, 2, 1])

    def test_dijkstra_down_path(self):
        path_act = Dj.build_path(1, 15)
        self.assertEqual(path_act, [15, 8, 1])

    def test_dijkstra_case_middle(self):
        path_act = Dj.build_path(1, 23)
        self.assertListEqual(path_act, [23, 16, 9, 2, 1])

    def test_get_dist_vertex_neig_cell(self):
        dist_act = Dj.get_distance_bw_vertex(1, 2)
        self.assertEqual(dist_act, 1)

    def test_get_dist_vertex_not_neig_cell(self):
        dist_act = Dj.get_distance_bw_vertex(1, 3)
        self.assertEqual(dist_act, 2)


class TestHexClass(unittest.TestCase):
    def test_hex_corner_x_creating(self):
        hex_zero_corner = hex_class.Hexagon.hex_corner(Point(0, 0), 3, 0)
        self.assertAlmostEqual(hex_zero_corner.x, 0 + 3 * math.cos(float(math.pi) / 180 * 30))

    def test_hex_corner_y_creating(self):
        hex_first_corner = hex_class.Hexagon.hex_corner(Point(0, 0), 3, 1)
        self.assertAlmostEqual(hex_first_corner.y, 0 + 3 * math.sin(float(math.pi) / 180 * (60 * 1 + 30)))

    def test_generating_hex_points(self):
        points_list = hex_class.Hexagon.generate_hex_points_list(Point(0, 0), 3)
        self.assertEqual(points_list[5].x, hex_class.Hexagon.hex_corner(Point(0, 0), 3, 6).x)

    def test_initialization(self):
        hexagon_object = hex_class.Hexagon(Point(0, 0), 3, "white", hide=False)
        self.assertEqual(hexagon_object.color, 'white')
        points = hex_class.Hexagon.generate_hex_points_list(Point(0, 0), 3)
        self.assertEqual(hexagon_object.centre.x, points[2].x + const_file.WIDTH_OF_HEX / 2)


class TestRecords(unittest.TestCase):
    def test_zero_seconds_are_thrown(self):
        lines = ['r 1', 'p 0', '']
        self.assertListEqual(list(filter(DataBase.is_time_zero, lines)), ['r 1'])

    def test_no__zero_seconds(self):
        lines = ['r 1', 'ppla 12', 'cale 33', 'manu 6']
        self.assertListEqual(list(filter(DataBase.is_time_zero, lines)), lines)

    def test_order_dictionary_function(self):
        dictionary = {'kate': 19, 'max': 1, 'violet': 3}
        self.assertEqual(DataBase.order_dictionary(dictionary), collections.OrderedDict({'max': 1, 'violet': 3, 'kate': 19}))

    def test_is_not_time_zero_function(self):
        time = ''
        self.assertFalse(DataBase.is_time_zero(time))

    def test_time_is_zero(self):
        self.assertFalse(DataBase.is_time_zero('p 0'))

    def test_formatting(self):
        db = DataBase
        with open("hex_testing.txt", 'w') as t:
            t.write("paolo 0\n")
            t.write("sena 0\n")
            t.write("lena 1\n")
            t.write("adolf 5")
        DataBase.format_data(db, 'hex_testing.txt')
        with open("hex_testing.txt", 'r') as t:
            lines = t.readlines()
        self.assertEqual(lines, ['lena 1\n', 'adolf 5\n'])


class TestFunctions(unittest.TestCase):
    def test_Game_unique_list(self):
        assert a_d.Functions.make_unique_list([[1, 2], [1, 2]]) == [[1, 2]]
        assert a_d.Functions.make_unique_list([[1, 2], [2]]) == [[1, 2], [2]]
        assert a_d.Functions.make_unique_list([[2, 3], [2], [3, 3], [2, 3]]) == [[2, 3], [2], [3]]
        assert a_d.Functions.make_unique_list([[]]) == [[]]

    def test_chain_done_horisontal(self):
        is_done = a_d.Functions.is_chain_done([1, 2, 3, 4, 5, 6, 7], const_file.ORIENTATIONS_DICTIONARY[const_file.player_one.color])
        assert is_done is True

    def test_chain_not_done_horisontal(self):
        is_done = a_d.Functions.is_chain_done([1, 2, 3, 4, 5, 7], const_file.ORIENTATIONS_DICTIONARY[const_file.player_one.color])
        assert is_done is False

    def test_chain_done_vertical(self):
        is_done = a_d.Functions.is_chain_done([1, 8, 15, 22, 29, 36, 43], const_file.ORIENTATIONS_DICTIONARY[const_file.player_two.color])
        assert is_done is True


    def test_chain_not_done_vertical(self):
        is_done = a_d.Functions.is_chain_done([1, 5, 7], const_file.ORIENTATIONS_DICTIONARY[const_file.player_two.color])
        assert is_done is False


if __name__ == '__main__':
    unittest.main()

