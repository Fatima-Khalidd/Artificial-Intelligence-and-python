import heapq
def uniform_cost_search(graph,start,goal):
    priority_queue=[]
    heapq.heappush(priority_queue,(0,start,[start]))
    visited_nodes=[]

    while priority_queue:
        #pop the node with lowest cost
        current_cost,current_node,current_path=heapq.heappop(priority_queue)

        #if this node is goal node, return the path
        if current_node==goal:
            return current_cost,current_path
        
        #if node has been visited with lower cost, skip it
        if current_node in visited_nodes and visited_nodes[current_node]<=current_cost:
            continue

        # mark node as visited with current_cost
        visited_nodes[current_node]=current_cost

        # Explore neighbours and push them into priority queue
    for neighbor, cost in graph[current_node].items(): 
            total_cost = current_cost + cost  # Calculate new cost
            heapq.heappush(priority_queue, (total_cost, neighbor, current_path + [neighbor]))

        # if no path is found, return failure 
    return float('inf'),[]
    




graph={
    'A':{'B':1, 'C':4},
    'B':{'A':1,'D':2,'E':5},
    'C':{'A':1, 'F':3},
    'D':{'B':2,'E':1},
    'E':{"B":5,'D':1,'F':2},
    'F':{'C':3,'E':2}
}

print(graph)
total_cost,path = uniform_cost_search(graph,'A',"F")
print('Total Cost',total_cost)
print('Path',path)