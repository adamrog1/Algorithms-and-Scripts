
nV = 5

INF = 999


def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    #pętla działa podobnie jak w drukowaniu tabliczki mnożenia, każda komórka tablicy jest sprawdzana
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_graph(distance)


def print_graph(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G =      [[0, 2, INF, 6, INF],
         [INF, 0, 3, 8, 5],
         [INF, INF, 0, INF, 7],
         [INF, INF, INF, 0, 9],
         [INF, INF, INF, INF, 0]]
floyd_warshall(G)
