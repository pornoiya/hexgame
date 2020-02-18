import collections
import const_file as const


class Functions:
    @staticmethod
    def make_unique_list(lst):
        unq_lst = collections.OrderedDict()
        for e in lst:
            unq_lst.setdefault(frozenset(e), []).append(e)
        return list(map(list, unq_lst.keys()))

    @staticmethod
    def is_chain_done(chain, orientation):
        if orientation == const.ORIENTATIONS_DICTIONARY[const.player_one.color]:
            dict = {}
            for ostatok in range(0, const.GRID_SIZE):
                dict.update({ostatok: -1})
            for item in chain:
                for ostatok in range(0, const.GRID_SIZE):
                    if item % const.GRID_SIZE != ostatok:
                        continue
                    elif item % const.GRID_SIZE == ostatok:
                        dict.update({ostatok: item})
                        break
            for value in dict.values():
                if value == -1:
                    return False
            return True
        elif orientation == const.ORIENTATIONS_DICTIONARY[const.player_two.color]:
            dict_r = {}
            for coefficient in range(0, const.GRID_SIZE):
                dict_r.update({coefficient: -1})
            for item in chain:
                for coefficient in range(0, const.GRID_SIZE):
                    if (item - 1) // const.GRID_SIZE != coefficient:
                        continue
                    elif (item - 1) // const.GRID_SIZE == coefficient:
                        dict_r.update({coefficient: item})
                        break
            for value in dict_r.values():
                if value == -1:
                    return False
            return True
