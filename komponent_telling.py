from graf_leser import Actor, Movie, adjacency_list_test

def bfs(key): #key is a movie node and item is a set og actors
    visited = [key] #Or seen
    been_to = []
    queue = [key]
    #current_node = key

    while len(queue) != 0:
        current_set = set()
        current_node = queue.pop()
        been_to.append(current_node)
        if isinstance(current_node, Actor):
            current_set = current_node._movie_set
        elif isinstance(current_node, Movie):
            current_set = current_node._actor_set
        
        for item in current_set:
            if item not in visited:
                visited.append(item)
                queue.append(item)
    return visited
                
def component_finding(adj): #adj is a dictionary
    components = []
    visited_list = []
    comp_dict = {}

    for key in adj.keys():
        if key in visited_list:
            continue
        partial_visited_list = bfs(key)
        components.append(partial_visited_list)
        visited_list = visited_list + partial_visited_list

    for component_partial_list in components:
        amount_actors_components = 0
        for element in component_partial_list:
            if isinstance(element, Actor):
                amount_actors_components += 1

        if amount_actors_components in comp_dict:
            #It will be a dict amount_actors --> amount of components with
            comp_dict[amount_actors_components] += 1 
        else:
            comp_dict[amount_actors_components] = 1
    return comp_dict

print(component_finding(adjacency_list_test))