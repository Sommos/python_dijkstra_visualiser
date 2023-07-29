import matplotlib.pyplot as plt
import networkx as nx

# create a graph for testing
G = nx.Graph()
# add nodes to the graph
G.add_edge("A", "B", weight = 4)
G.add_edge("A", "C", weight = 2)
G.add_edge("B", "C", weight = 5)
G.add_edge("B", "D", weight = 10)
G.add_edge("C", "D", weight = 3)
G.add_edge("D", "E", weight = 7)
G.add_edge("E", "F", weight = 6)

def create_graph():
    # create a graph
    G = nx.Graph()

    # add user defined nodes to the graph
    num_nodes = int(input("Enter the number of nodes you would like in your graph: "))
    # loop through the number of nodes, and ask the user to name each node
    for i in range(num_nodes):
        node_name = input(f"Enter the name of node {i + 1}: ")

    # add user defined edges to the graph
    num_edges = int(input("Enter the number of edges you would like in your graph: "))
    # loop through the number of edges, and ask the user to define each edge
    for i in range(num_edges):
        # ask the user to define the edge, along with the weight of the edge
        edge_info = input(f"Enter edge {i + 1} (format: 'source_node target_node weight'): ")
        # split the user input into the source node, target node, and weight
        source, target, weight = edge_info.split()
        # add the edge to the graph
        G.add_edge(source, target, weight = int(weight))
    
    # return the graph
    return G

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

    # return the distances dictionary 
    return distances

def visualise_dijkstra(graph, start):
    # check if start node is in the graph
    if start not in graph.nodes:
        print("Start node not found in graph")
        return
    
    distances, paths = dijkstra(graph, start)
    pos = nx.spring_layout(graph)
    # draw the graph with basic styling
    nx.draw(graph, pos, with_labels = True, node_color = "skyblue", node_size = 1500, font_size = 10, font_weight = "bold")
    # build labels for the nodes
    labels = nx.get_edge_attributes(graph, "weight")
    # draw the labels onto the graph
    nx.draw_networkx_edge_labels(graph, pos, edge_labels = labels, font_size = 8)

    plt.title("Dijkstra's Algorithm Visualisation")
    plt.show()

    print("Shortest distances from the start node:")
    # loop distances dictionary and print the distance of each node from the start node
    for node, distance in distances.items():
        print(f"{node}: {distance}")

    print("Shortest paths from the start node:")
    # loop paths dictionary and print the path of each node from the start node
    for node, path in paths.items():
        print(f"{node}: {' -> '.join(path)}")

if __name__ == "__main__":
    user_graph = create_graph()
    start_node = input("Enter the start node: ")
    visualise_dijkstra(user_graph, start_node)