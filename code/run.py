# Search methods

import search
import utils

ab = search.GPSProblem('A', 'B', search.romania)
cz = search.GPSProblem('C', 'Z', search.romania)
ds = search.GPSProblem('D', 'S', search.romania)
li = search.GPSProblem('L', 'I', search.romania)
nu = search.GPSProblem('N', 'U', search.romania)

problems = [ab, cz, ds, li, nu]

print("BFS A->B")
print(search.breadth_first_graph_search(ab).path())  # BFS
print("DFS A->B")
print(search.depth_first_graph_search(ab).path())  # DFS
print("---------------------")
print()
print("comparación de búsquedas con/sin subestimación")
print()
for problem in problems:
    print(problem.initial," -> ",problem.goal)
    print("no heuristic")
    print(search.dijkstra(problem).path())  # Dijkstra/RyA
    print()
    print("with heuristic")
    print(search.heap_heuristic_graph_search(problem).path())  # RyAsub
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print()

# Conclusión:
# Dijkstra y subestimación con heuristica dan el mismo camino, que queremos.
# Con la heurística expandemos menos nodos (en caso de AB, 24 vs 6).

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
