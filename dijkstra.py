import const_file as c


class Dj:
    @staticmethod
    def generate_neighbors(cell, GRID_SIZE=c.GRID_SIZE):
        if cell == 1:
            data = {GRID_SIZE + 1, 2}
        elif cell == GRID_SIZE ** 2:
            data = {cell - GRID_SIZE, cell - 1}
        elif cell == GRID_SIZE:
            data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
        elif cell == GRID_SIZE ** 2 - GRID_SIZE + 1:
            data = {cell + 1, cell - GRID_SIZE, cell - GRID_SIZE + 1}
        elif cell < GRID_SIZE:
            data = {cell + 1, cell - 1, cell + GRID_SIZE,
                    cell + GRID_SIZE - 1}
        elif cell > GRID_SIZE ** 2 - GRID_SIZE:
            data = {cell + 1, cell - 1,
                    cell - GRID_SIZE, cell - GRID_SIZE + 1}
        elif cell % GRID_SIZE == 0:
            data = {cell + GRID_SIZE, cell - GRID_SIZE, cell - 1,
                    cell + GRID_SIZE - 1}
        elif cell % GRID_SIZE == 1:
            data = {cell - GRID_SIZE + 1, cell - GRID_SIZE,
                    cell + 1, cell + GRID_SIZE}
        else:
            data = {cell - 1, cell + 1, cell - GRID_SIZE, cell + GRID_SIZE, cell + GRID_SIZE - 1,
                    cell - GRID_SIZE + 1}
        return data

    @staticmethod
    def get_distance_bw_vertex(cell_main=1, cell_to_compare=49):
        if cell_to_compare != cell_main:
            depth = 1
            neigs = list(Dj.generate_neighbors(cell_to_compare))
            checked = []
            while cell_main not in neigs:
                depth = depth + 1
                for neig_cell in neigs:
                    if neig_cell not in checked:
                        neigs = list(set(neigs + list(Dj.generate_neighbors(neig_cell))))
                        checked.append(neig_cell)
                        neigs.remove(neig_cell)
            return depth
        else:
            return 0

    for cell in range(1, c.GRID_SIZE ** 2 + 1):
        if cell in c.clicked:
            c.visited.add(cell)
        c.d.update({cell: 1})
        if cell != c.cell_beg:
            c.mark.update({cell: 10000})
        else:
            c.mark.update({cell: 0})

    @staticmethod
    def chose_min(mark):
        min_v = 10000
        cell_min_value = 1
        for i in range(1, c.GRID_SIZE**2+1):
            if i not in c.visited and mark[i] < min_v:
                min_v = mark[i]
                cell_min_value = i
        return cell_min_value

    @staticmethod
    def dijkstra(mark):
        while len(c.visited) != c.GRID_SIZE**2:
            cell_min_value = Dj.chose_min(mark)
            for neig in Dj.generate_neighbors(cell_min_value):
                if 1 + mark[cell_min_value] < mark[neig]:
                    mark.update({neig: 1 + mark[cell_min_value]})
                    c.d.update({neig: cell_min_value})
            c.visited.append(cell_min_value)
            #c.visited.add(cell_min_value)
            Dj.dijkstra(mark)
        return c.d

    @staticmethod
    def build_path(start, end):
        res = [end]
        dist = Dj.dijkstra(c.mark)
        while end != start:
            res.append(dist[end])
            end = dist[end]
        return res
