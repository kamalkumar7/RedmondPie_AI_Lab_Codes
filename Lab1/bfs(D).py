# CS362 Artificial Intelligence
# Lab assignment 1: code for problem (D)

# Team: Redmond pie
# Member 1: Kamal Kumar (202051098)
# Member 2: Apoorv Pathak (202051033)
# Member 3: Aryan Gupta (202051038)
# Member 4: Tejas Joshi (202051091)

from collections import defaultdict as dd

class Graph:

    def __init__(self):
        self.graph = dd(list)
        self.parent = dd(int)
        self.distance = dd(int)
        self.frontier = list()

    def set_distance(self, node):
        self.distance[node] = -1

    # method to add edges in the BFS graph
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    # method to backtrack and generate the path
    def get_path(self, start, goal):
        path, node = [], goal
        while node != start:
            path.append(node)
            node = self.parent[node]
        path.append(start)
        path.reverse()
        return path

    # method to implement BFS
    def bfs(self, start, goal):
        self.distance[start] = 0
        self.frontier.append(start)
        while len(self.frontier) != 0:
            a = self.frontier.pop(0)
            for b in self.graph[a]:
                if self.distance[b] == -1:
                    self.distance[b] = self.distance[a] + 1
                    self.parent[b] = a
                    self.frontier.append(b)
        distance = self.distance[goal]
        if distance != -1:
            path = self.get_path(start, goal)
        else:
            path = None
        return path, distance

def main():
    print('\nBreadth First Search (BFS)')
    print('\nNOTE:')
    print('1. Each of the following input lines require spaced separated entries.')
    print('2. Nodes are numbered from 1 to N by the program, where N is the total number of nodes.')
    graph = Graph()
    num_nodes, num_edges = [int(x) for x in input('\nEnter number of nodes, number of edges: ').split()]
    for i in range(1, num_nodes + 1):
        graph.set_distance(i)
    print('\n')
    for i in range(num_edges):
        a, b = [int(x) for x in input('Enter initial node, end node of edge ' + str(i + 1) + ': ').split()]
        graph.add_edge(a, b)
    start, goal = [int(x) for x in input('\nEnter start node, goal node: ').split()]
    path, distance = graph.bfs(start, goal)
    if distance == -1:
        print('\nPath from start node to goal node does not exist.\n')
    else:
        path_route = ' --> '.join([str(x) for x in path])
        print('\nPath from start node to goal node: ', path_route)
        print('Total path distance: ', distance, '\n')

if __name__ == '__main__':
    main()
