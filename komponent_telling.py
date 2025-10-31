from graf_leser import Actor, adjacency_list_test
from collections import deque, Counter

def bfs(adj, start_node): #key is a movie node and item is a set og actors
    visited = set() #Or seen
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        current = queue.popleft()
        neighbours = adj.get(current, set()) #Returns set in case there isn't a value for the key
        for item in neighbours:
            if item not in visited:
                visited.add(item)
                queue.append(item)
    return visited
                
def component_finding(adj): #adj is a dictionary
    visited = set()
    counter = Counter()

    for node in adj.keys():
        if node in visited:
            continue
        component = bfs(adj, node)
        visited.update(component)

        actor_count = sum(1 for n in component if isinstance(n, Actor))
        counter[actor_count] += 1

    return dict(counter)

def print_component_sizes(comps):
    sorted_comps = dict(sorted(comps.items(), reverse=True))
    for key, value in sorted_comps.items():
        if key == 0:
            continue
        print(f"There are {value} components of size {key}")

if __name__ == "__main__":
    print_component_sizes(component_finding(adjacency_list_test))