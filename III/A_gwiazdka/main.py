
class Apirm:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list


    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1
        }

        return H[n]


    def get_neighbors(self, v):
        return self.adjacency_list[v]

#algorytm jest dłuższy ale za to odnajdywanie najszybszej drogi jest znacznie szybsze niż np. przy algorytmie Djikstry
    def a_gwiazdka_algorithm(self, start_node, stop_node):
        open_list = {start_node}
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print('Droga nie isnieje')
                return None
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Najkrótsza droga znaleziona przez: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)

        return None

adjacency_list = {
        'A': [('B', 2), ('D', 6)],
        'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
        'C': [('B', 3), ('E', 7)],
        'D': [('A', 6), ('B', 8), ('E', 9)],
        'E': [('B', 5), ('C', 7), ('D', 9)]
    }
graph1 = Apirm(adjacency_list)
graph1.a_gwiazdka_algorithm('A', 'E')