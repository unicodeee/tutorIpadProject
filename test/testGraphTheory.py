from collections import defaultdict

# Represent the graph as an adjacency list
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'M'],
    'C': ['B', 'D'],
    'D': ['C', 'F'],
    'F': ['D', 'G'],
    'G': ['F', 'H'],
    'H': ['G', 'J'],
    'J': ['H', 'K'],
    'K': ['J'],
    'M': ['B', 'C', 'X', 'Y', 'Z'],
    'X': ['M', 'Y'],
    'Y': ['M', 'X', 'Z'],
    'Z': ['M', 'Y']
}

def dfs(node, visited, group):
    stack = [node]
    count = 3
    while stack and count > 0:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            group.append(current_node)
            stack.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)
            count -= 1

def find_groups():
    visited = set()
    groups = []

    for node in graph:
        if node not in visited:
            group = []
            dfs(node, visited, group)
            groups.append(group)

    return groups

groups = find_groups()
group_count = 0

group_result = []

for group in groups:
    if len(group) <= 3:
        group_count += 1
        group_result.append(group)
        print(f"Group {group_count}: {group}")

# Check if the groups can be divided into 7 or fewer isolated groups
if group_count <= 7:
    print("It's possible to cut the graph into groups of 3 or less with a total of no more than 7 isolated groups.")
else:
    print("It's not possible to meet the specified conditions.")

print("Group Sizes:", [len(group) for group in group_result])
