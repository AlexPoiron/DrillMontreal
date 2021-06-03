def nedge(a, b):
    return (a, b) if a < b else (b, a)

#Create the list of edges from a matrix representing a graph
def mat_to_edges(mat):
    edges = []
    for i in range(len(mat)):
        for j in range(i):
            if (mat[i][j] != 0):
                edges.append((i, j))
    return edges

def find_eulerian_cycle_rec( edges, frome, to, res):
    res.append(frome)
    if (frome,to) in edges:
        edges.remove((frome, to))
    else:
        edges.remove((to, frome))
    if (to, to) in edges:
        print("a")
        find_eulerian_cycle_rec(edges, to, to, res)
    else:
        for (a,b) in edges:
            if a == to:
                print("b")
                find_eulerian_cycle_rec(edges, a, b, res)
            elif b == to:
                print("c")
                find_eulerian_cycle_rec(edges, b, a, res)
    print("res ", res)
    return res

def passing(elem, tmp, edges):
    if (tmp[elem] == 0):
        tmp[elem] = 1
        for i in range (len(edges)):
            if (edges[i][0] == elem):
                passing(edges[i][1], tmp, edges)
            if (edges[i][1] == elem):
                passing(edges[i][0], tmp, edges)

def is_edge_connected(n, edges):
    tmp = [2] * n
    if (n ==0 or len(edges) == 1):
        return True
    for i in range (len(edges)):
        (a, b) = edges[i]
        tmp[a] = 0
        tmp[b] = 0
    passing(0, tmp, edges)
    for i in range (n):
        if (tmp[i] == 0):
            return False
    return True

def is_eulerian_cycle(m, edges, cycle):
    if (is_edge_connected(m, edges) == False):
        return False
    for i in range(0, len(cycle)):
        if i == len(cycle) - 1:
            (a,b) = (cycle[i] , cycle[0])
        else:
            (a,b) = (cycle[i] , cycle[i+1])
        if (a,b) in edges:
            edges.remove((a,b))
        else:
            if (b,a) in edges:
                edges.remove((b,a))
            else:
                return False
    if len(edges) == 0:
        return True
    return False

#assert edges1 == [(2, 0), (2, 1), (3, 1), (3, 2)]

#assert edges2 == [(1, 0), (3, 2), (4, 1), (4, 2), (4, 3)]

#assert edges3 == [(1, 0), (2, 0), (2, 1), (3, 0), (4, 0), (4, 3)]