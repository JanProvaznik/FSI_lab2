# Search methods

import search
import utils

ab = search.GPSProblem('A', 'B', search.romania)
cz = search.GPSProblem('C', 'Z', search.romania)
ds = search.GPSProblem('D', 'S', search.romania)
li = search.GPSProblem('L', 'I', search.romania)

print(search.breadth_first_graph_search(ab).path()) #BFS
print(search.depth_first_graph_search(ab).path()) #DFS
print("---------------------")

print(search.dijkstra(ab).path()) #Dijkstra/RyA
print(search.heuristic_graph_search(ab).path()) #RyAsub
print("+++++++++++++")


print(search.dijkstra(cz).path()) #Dijkstra/RyA
print(search.heuristic_graph_search(cz).path()) #RyAsub
print("+++++++++++++")

print(search.dijkstra(ds).path()) #Dijkstra/RyA
print(search.heuristic_graph_search(ds).path()) #RyAsub

print("+++++++++++++")
print(search.dijkstra(li).path()) #Dijkstra/RyA
print(search.heuristic_graph_search(li).path()) #RyAsub
# Conclusión:
# Dijkstra y heuristica dan el mismo camino, que queremos.
# Con la heurística expandemos menos nodos (en caso de AB, 24 vs 6).

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
