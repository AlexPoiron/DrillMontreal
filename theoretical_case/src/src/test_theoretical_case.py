import theoretical_case as tc
from graph import Graph

graph1 = [[0,0,1,0],
          [0,0,1,1],
          [1,1,0,1],
          [0,1,1,0]]


graph2 = [[0,1,0,0,0],
          [1,0,0,0,1],
          [0,0,0,1,1],
          [0,0,1,0,1],
          [0,1,1,1,0]]



graph3 = [[0,1,1,1,1],
          [1,0,1,0,0],
          [1,1,0,0,0],
          [1,0,0,0,1],
          [1,0,0,1,0]]

graph4 = [[0,1,0,1],
          [1,0,1,0],
          [0,1,0,1],
          [1,0,1,0]]


edges1 = tc.mat_to_edges(graph1)
#print(edges1)

edges2 = tc.mat_to_edges(graph2)
#print(edges2)

edges3 = tc.mat_to_edges(graph3)
#print(edges3)

assert edges1 == [(2, 0), (2, 1), (3, 1), (3, 2)]

assert edges2 == [(1, 0), (3, 2), (4, 1), (4, 2), (4, 3)]

assert edges3 == [(1, 0), (2, 0), (2, 1), (3, 0), (4, 0), (4, 3)]

g2 = Graph([(2,0),(2,1),(3,1),(1,2),(0,2),(2,3),(3,0),(3,2),(0,1),(0,0)], 4)

print("hi", tc.is_eulerian_cycle(g2.get_nb_nodes(), g2.get_edges(), g2.find_eulerian_cycle()))

#assert tc.is_eulerian_cycle(g.get_edges(), g.find_eulerian_cycle()) == True


#print(g.find_eulerian_cycle())
