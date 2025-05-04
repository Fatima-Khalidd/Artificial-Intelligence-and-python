def a_star_algorithm(graph, start, goal, heuristic):
    # Open list (nodes to be evaluated) and closed list (nodes already evaluated)
    open_list = []  # List of nodes to be evaluated
    closed_list = []  # List of nodes already evaluated

    # Add the start node to the open list with initial costs
    open_list.append((start, 0, heuristic[start]))  # (node, g cost, h cost)

    while open_list:
        # Sort the open list to get the node with the lowest f value (g + h)
        open_list.sort(key=lambda x: x[1] + x[2])  # Sort by f = g + h
        current_node, g_cost, h_cost = open_list.pop(0)  # Node with the lowest f value

        # If we reach the goal, reconstruct the path
        if current_node == goal:
            path = [current_node]
            return path  # Return the path (just the goal node in this case)

        # Move the current node from open to closed list
        closed_list.append(current_node)

        # Get neighbors of the current node
        neighbors = graph[current_node]

        for neighbor, cost in neighbors.items():
            # If the neighbor is in the closed list, skip it
            if neighbor in closed_list:
                continue

            # Calculate the g cost for the neighbor
            new_g_cost = g_cost + cost  # Cost from start to neighbor

            # Check if the neighbor is already in the open list
            # If it is, we need to check if the new path is better
            existing_node = next((x for x in open_list if x[0] == neighbor), None)

            if existing_node is None:
                # If the neighbor is not in the open list, add it
                open_list.append((neighbor, new_g_cost, heuristic[neighbor]))
            else:
                # If the neighbor is in the open list, check if the new path is better
                if new_g_cost < existing_node[1]:
                    # Update the neighbor's g cost and h cost
                    open_list.remove(existing_node)
                    open_list.append((neighbor, new_g_cost, heuristic[neighbor]))

    return None  # Return None if no path is found
 
# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Example heuristic values (straight-line distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 0
}

# Run the A* algorithm
start_node = 'A'
goal_node = 'E'
path = a_star_algorithm(graph, start_node, goal_node, heuristic)

# Print the result
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")









def a_star(graph,start,goal,heuristic):
    open_list=[]
    closed_list=[]

    open_list.append(start,0,heuristic[start])
    while open_list:
        open_list.sort(key=lambda x: x[1]+x[2])
        current_node,g_cost,h_cost=open_list.pop()

        if current_node==goal:
            path=current_node
            return path
        
        closed_list.append(current_node)
        neighbour =graph[current_node]

        for neighbour , cost in neighbour.items():
            if neighbour in closed_list:
                continue

            new_g_cost=g_cost+h_cost

            existing_node=next((x for x in open_list if neighbour=x[1]),None)

            if existing_node is None:
                open_list.append(neighbour,new_g_cost,heuristic[neighbour])
            else:
                if new_g_cost<existing_node[1]:
                    open_list.remove(existing_node)
                    open_list.append(neighbour,new_g_cost,heuristic[neighbour])

    return None 



def a_star_algo(graph,start,goal,heuristic):
    open_list=[]
    closed_list=[]
    
    open_list.append(start,0,heuristic[start])

    while open_list:
        open_list.sort(key=lambda x:x[1]+x[2])
        current_node,g_cost,h_cost=open_list.pop()

        if current_node==goal:
            path=current_node
            return path
        
        closed_list=[current_node]

        neighbour=graph[current_node]

        for neighbour,cost in neighbour.items():
            if neighbour in closed_list:
                continue

            new_g_cost=h_cost+g_cost

            existing_node=next ((x for x in open_list if neighbour==x[0]),None)

            if existing_node==None:
                open_list.append(neighbour,new_g_cost,heuristic[neighbour])

            else:
                if new_g_cost<existing_node[1]:
                    open_list.remove(existing_node)
                    open_list.append(neighbour,new_g_cost,heuristic[neighbour])

    return None




 
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Example heuristic values (straight-line distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 0
}

# Run the A* algorithm
start_node = 'A'
goal_node = 'E'
path = a_star_algorithm(graph, start_node, goal_node, heuristic)

# Print the result
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")

