from six_degrees import *
from graf_leser import Actor, Movie, adjacency_list_test

def chilleste_vei(adj, start_id, end_id): 
    node_list = id_to_node(start_id, end_id)
    start_node = node_list[0]
    end_node = node_list[1]
    tie_breaker = 0

    if not both_nodes_in_component(adj, start_node, end_node):
        return "Nodes ain't connected love amen"

    open_heap = [(0, tie_breaker, start_node)] #(cost, node)
    # heapq.heapify(open_heap) 
    closed_set = set()
    seen_nodes = {start_node: (0, "")} #A tuple of the cost and parent 

    while len(open_heap) != 0: 
        current_node = heapq.heappop(open_heap)[2] #the lowest cost lies in [0]
        if current_node == end_node:
            break
        
        if current_node in closed_set:
            continue
        closed_set.add(current_node)
        for n in adj.get(current_node, set()):
            if n in closed_set:
                continue
            
            given_cost = 0 if isinstance(n, Actor) else (10.0 - float(n._rating))
            tentative_cost = seen_nodes[current_node][0] + given_cost
            if n in seen_nodes.keys():
                if tentative_cost < seen_nodes[n][0]:
                    seen_nodes[n][0] = tentative_cost
                    seen_nodes[n][1] = current_node #Sets new parent
            else: 
                seen_nodes[n] = (tentative_cost, current_node)
            
            if n not in closed_set:
                tie_breaker += 1
                heapq.heappush(open_heap, (seen_nodes[n][0], tie_breaker, n)) #If not seen then should be explored 
    return find_path(current_node, seen_nodes)

chill_vei = chilleste_vei(adjacency_list_test, "nm0000313", "nm0140504")
print_path(chill_vei)



