import theoretical_case as tc

class Graph:

    def __init__(self, edges, nb_nodes):
        self.edges = edges
        self.nb_nodes = nb_nodes
    
    def find_eulerian_cycle(self):
        res = []
        if (len(self.edges) == 0):
            return res
        tmp = self.edges[:]
        m = 8
        res = tc.find_eulerian_cycle_rec(tmp, self.edges[0][0], self.edges[0][1], res)
        return res

    def get_edges(self):
        return self.edges
    
    def get_nb_nodes(self):
        return self.nb_nodes

    