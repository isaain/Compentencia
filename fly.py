from collections import deque
from heapq import heappop, heappush
from math import inf

class Graph:
    def __init__(self, size: int) -> None:
        self.size = size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        """
        Add an edge from `u` to `v` with the given `weight`, or `1` if no `weight` is provided.
        """
        self.adj[u].append((weight, v))

    def dijkstra(self, start: int) -> list[float]:  # O((V + E) log V)
                """
                Find the length of the shortest path from the `start` node to all other nodes.
                """
                distance = [inf] * self.size
                distance[start] = 0
                priority_queue = [(0, start)]
        
                while priority_queue:
                    d1, node = heappop(priority_queue)
        
                    if d1 > distance[node]:
                        continue
        
                    for weight, neighbor in self.adj[node]:
                        if distance[node] + weight < distance[neighbor]:
                            distance[neighbor] = distance[node] + weight
                            heappush(priority_queue, (distance[neighbor], neighbor))
        
                return distance


def main() -> None:
    n, m = map(int, input().split())
    grafo = Graph(n)
    for i in range(0, m):
         nodo1, nodo2, peso = map(int, input().split())
         grafo.add_edge(nodo1-1, nodo2-1, peso)

    lista = grafo.dijkstra(0)
    print(lista)
    lista = lista[::-1]
    lista2 = []
    for item in lista:
        if lista.index(item) != len(lista):
            lista2[item] = lista[item] - lista[item+1]

    mayor = max(lista2)
    indice = lista2.index(mayor)
    reserva = int(lista2[indice]/2)
    lista2[indice] = lista2[indice]/2
    if lista2 < reserva:
        lista2[indice] = int(lista2) - 1
    suma = 0
    for item in lista2:
        suma += lista2[item]
    print(suma)
if __name__ == "__main__":
    main()