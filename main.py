import matplotlib.pyplot as plt
import networkx as nx

# create a graph
G = nx.Graph()
# add nodes to the graph
G.add_edge("A", "B", weight = 4)
G.add_edge("A", "C", weight = 2)
G.add_edge("B", "C", weight = 5)
G.add_edge("B", "D", weight = 10)
G.add_edge("C", "D", weight = 3)
G.add_edge("D", "E", weight = 7)
G.add_edge("E", "F", weight = 6)

def dijkstra(graph, start):
    # initialize the distance of each node to infinity
    distances = {node: float("inf") for node in graph.nodes}
    # the distance from the start node to itself is 0
    distances[start] = 0
    # initialize an empty dictionary for the path
    visited = set()
    # loop while there are nodes to visit
    while len(visited) < len(graph.nodes):
        # get the candidates for the next step
        candidates = {node: distances[node] for node in graph.nodes if node not in visited}
        # get the node with the minimum distance
        min_node = min(candidates, key = candidates.get)
        # add the minimum distance node to the visited nodes set
        visited.add(min_node)
        # loop through the neighbors of the minimum distance node
        for neighbor, weight in graph[min_node].items():
            # if the distance from the start node to the neighbor node is greater than the distance 
            # from the start node to the minimum distance node plus the weight of the edge between 
            # the minimum distance node and the neighbor node
            distances[neighbor] = min(distances[neighbor], distances[min_node] + weight["weight"])
        
    return distances

