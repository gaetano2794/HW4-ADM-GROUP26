import heapq
import networkx as nx
from collections import *



def shortestPath(G, source, target):
    # Check whether input author exists in graph
    if G.has_node(target) == False:
        return ("Node " + str(target) + " is NOT in the graph.")

    # Check whether there is a path from input author to Aris
    if not nx.has_path(G, source, target):
        return "There is no path from " + str(source) + " to " + str(target)

    # Initialize queue
    Q = []
    heapq.heappush(Q, (0, source))

    # Keep track of visited nodes
    D = {aut: None for aut in G.nodes()}

    while Q:
        # repeat while Q is not empty
        t = heapq.heappop(Q)  # pop the current node ,t, associated with minumum distance

        if t[1] == target:
            return "The weight of the shortest path from " + str(source) + " to " + str(target) + " is: " + str(t[0])

        # If  t has already been visited, it does not make sense to update all the distances again.
        if D[t[1]] is None:
            # update D to indicate that node t has been visited
            D[t[1]] = t[0]

            # Compute tentative distance for all the unvisited neighbours of current minumum distance node
            # push it into the heap
            for neig in G[t[1]].keys():
                if D[neig] is None:
                    heapq.heappush(Q, (G[t[1]][neig]["weight"] + t[0], neig))



def shortestPath_all(G, q):  # target

    allpaths = defaultdict(list)

    # iterate through all the nodes in the set q
    for source in q:

        # initialize queue
        Q = []
        heapq.heappush(Q, (0, source))

        # keep track of visited node
        D = {aut: None for aut in G.nodes()}

        while Q:  # repeat while Q is not empty
            t = heapq.heappop(Q)

            allpaths[t[1]].append(t[0])  # append shortest path weight between source and t

            # if t has already been visited, it does not make sense to update all the distances again
            if D[t[1]] is None:
                # updated visited nodes
                D[t[1]] = t[0]
                # update distances related to the unvisited neighbours of t and push them in the heap Q.
                for neig in G[t[1]].keys():
                    if D[neig] is None:
                        heapq.heappush(Q, (G[t[1]][neig]["weight"] + t[0],
                                           neig))  # there could be more distances for the same node, but the smallest always come first

    # store all the node ids
    nodes = list(allpaths.keys())
    # extract the minumum of all the lists representing the values of the dictionary allpaths.
    minimums = list(map(min, allpaths.values()))
    # create and return the dictionary described above
    return dict(zip(nodes, minimums))