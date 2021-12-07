import sys


class Dijkstra():
    # Algorytm jest bardzo podobny do algorytmu prima wszystkie początkowe funkcje są identyczne jak w przypadku Prima czyli mamy kontruktor z ilością węzłów,
    # metoda od wyswietlania, minimalny klucz
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for c in range(vertices)]
                      for r in range(vertices)]

    def print(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print("węzeł", node, "koszt", dist[node])

    def minKey(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # tutaj widac różnice od algorytmu Prima, ten skupia się bardziej na odnalezieniu scieżki o najmniejszym całkowitym koszcie "podróży"
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minKey(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print(dist)


g = Dijkstra(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0],
           ]

g.dijkstra(0)
