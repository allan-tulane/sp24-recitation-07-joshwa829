from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        curr_node = frontier.pop()
        near_nodes = graph[curr_node]
        for node in near_nodes:
            if node not in result:
                result.add(node)
                frontier.add(node)
    return result





def connected(graph):
    prev_nodes = reachable(graph, list(graph.keys())[0])
    if len(graph) == len(prev_nodes):
      return True
    return False




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    
    prev_nodes = set()  
    count = 0
    for node in graph:
      if node not in prev_nodes:
        current_visited = reachable(graph, node)
        prev_nodes.update(current_visited)
        count += 1  
    return count

