import itertools


class Graph(object):
    """docstring for Graph."""
    def __init__(self, edge_list):

        self.edge_list = edge_list

        self.edge_a = edge_list[0]
        self.edge_b = edge_list[1]
        self.edge_c = edge_list[2]
        self.edge_d = edge_list[3]
        self.edge_e = edge_list[4]
        self.edge_f = edge_list[5]
        self.edge_g = edge_list[6]
        self.edge_h = edge_list[7]
        self.edge_i = edge_list[8]
        self.edge_j = edge_list[9]

        self.node1 = self.edge_a * self.edge_b * self.edge_c
        self.node2 = self.edge_a * self.edge_d * self.edge_e
        self.node3 = self.edge_j * self.edge_e
        self.node4 = self.edge_b * self.edge_h
        self.node5 = self.edge_c * self.edge_f
        self.node6 = self.edge_g * self.edge_d
        self.node7 = self.edge_i * self.edge_j * self.edge_f
        self.node8 = self.edge_h * self.edge_i * self.edge_g

        self.score = self.node1 + self.node2 + self.node3 + self.node4 + self.node5 + self.node6 + self.node7 + self.node8

        self.node_list = [self.node1, self.node2, self.node3, self.node4, self.node5, self.node6, self.node7, self.node8]


if __name__ == '__main__':

    primes = [2,3,5,7,11,13,17,19,23,29]
    best_score = 999999

    for primes_list in itertools.permutations(primes):
        new_graph = Graph(primes_list)

        if new_graph.score < best_score:
            best_score = new_graph.score
            best_graph = new_graph


    print(best_graph.score)
    print(best_graph.node_list)
