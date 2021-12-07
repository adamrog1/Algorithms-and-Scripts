
class Prim():
#zmienna vetices określa ilosc węzłów, potem graph tworzy graf
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for c in range(vertices)]
                      for r in range(vertices)]

#print wyświetla scieżkę naszego algorytmu
    def print(self, parent):
        print("Ścieżka wygląda nastepująco: \t")
        print ("Węzeł \tSiła")
        for i in range(1,self.V):
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])

#metoda która pozwala określić nam w którą strone ma podąrzyć algorytm, określa która sćieżka ma najmniejszy numerek(wagę)
    def minKey(self, key, mstSet):
        min = 1000000
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

#główna metoda algorytmu
    def primMST(self):
        key = [1000000] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                #sprawdzamy komórki
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        self.print(parent)


g = Prim(5)
#graf połączeń, działa na zasadzie 0 kolumna to 0 węzeł i po kolei 0 jest połączone : nie ze soba, z 1 o sile 2, nie z 2, z 3 o sile 6 i nie z 4 itd.
g.graph = [  [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
           ]
#w tym przpadku algorytm zadziała: od 0 do 1 ponieważ wybierze wage 2 zamiast 6, od 1 do 2  bo wybierze 3, potem do węzła 3 z 0 bo połączenie z 0 ma wage 6 a z jedynki 8 i na końcu do 4 najmniejsza wage ma 5 przy węźle 1
g.primMST();