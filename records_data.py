import collections


class DataBase:
    NAME_SCORE = {}

    def format_data(self, file):
        with open(file, 'r') as f:
            lines = filter(DataBase.is_time_zero, f.read().splitlines())
            for line in lines:
                name = line.split(' ')[0]
                score = int(line.split(' ')[1])
                d = self.NAME_SCORE
                if name in d.keys():
                    if d[name] > score:
                        d.update({name: score})
                else:
                    d.update({name: score})
            sd = collections.OrderedDict(DataBase.order_dictionary(d))
        f = open(file, 'w')
        for item in sd.items():
            f.write(item[0] + ' ' + str(item[1]) + '\n')
        f.close()

    @staticmethod
    def order_dictionary(d):
        list_dict = list(d.items())
        list_dict.sort(key=lambda l: l[1])
        return dict(list_dict)

    @staticmethod
    def is_time_zero(line):
        return line != '' and int(line.split(' ')[1]) != 0

