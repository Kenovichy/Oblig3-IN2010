from graf_leser import Actor, Movie, adjacency_list_test
import math
import heapq
from collections import deque, Counter
from komponent_telling import bfs

def both_nodes_in_component(adj, start_node, end_node):
    visited_set = bfs(adj, start_node)
    if end_node in visited_set:
        return True
    return False

def find_path(node, node_dict):
    path = [node]
    current_node = node
    while node_dict[current_node][1] != "":
        parent = node_dict[current_node][1]
        path.append(str(parent))
        current_node = parent
    path.reverse()
    return path

def id_to_node(start_id, end_id):
    for key in adjacency_list_test.keys():
        if key.return_id() == start_id:
            start_node = key
        elif key.return_id() == end_id:
            end_node = key
    return (start_node, end_node)

#Vi bruker Djikstra
def find_end_node(adj, start_id, end_id):
    node_list = id_to_node(start_id, end_id)
    start_node = node_list[0]
    end_node = node_list[1]
    tie_breaker = 0
    if not both_nodes_in_component(adj, start_node, end_node):
        return "Nodes ain't connected love amen"

    open_heap = [(0, tie_breaker, start_node)] #(cost, node)
    heapq.heapify(open_heap) 
    closed_set = set()
    seen_nodes = {start_node: (0, "")} #A tuple of the cost and parent 

    while len(open_heap) != 0: 
        current_node = heapq.heappop(open_heap)[2] #the lowest cost lies in [0]
        if current_node == end_node:
            break
        
        closed_set.add(current_node)
        for n in adj.get(current_node, set()):
            if n in closed_set:
                continue

            tentative_cost = seen_nodes[current_node][0] + 1 
            if n in seen_nodes.keys():
                if tentative_cost < seen_nodes[n][0]:
                    seen_nodes[n][0] = tentative_cost
                    seen_nodes[n][1] = current_node #Sets new parent
            else: 
                seen_nodes[n] = (tentative_cost, current_node)
            
            if n not in closed_set:
                tie_breaker += 1
                heapq.heappush(open_heap, (seen_nodes[n][0],tie_breaker, n)) #If not seen then should be explored 
    amount_of_edges = len(find_path(current_node, seen_nodes))
    return f"It takes {amount_of_edges - 1} connections to get from {start_node} to {end_node}"

answer = find_end_node(adjacency_list_test, "nm0000313", "nm0140504")
print(answer)
         





