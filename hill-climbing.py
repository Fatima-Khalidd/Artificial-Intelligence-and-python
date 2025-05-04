successor_list = {
    ('A', 5): [('B', 2), ('C', 4)],
    ('B', 2): [('D', 2), ('E', 3)],
    ('C', 4): [('F', 2), ('G', 4)],
    ('D', 2): [('H', 1), ('I', 99)],
    ('F', 2): [('J', 99)],
    ('G', 4): [('K', 99), ('L', 3)]
}

closed = []

def movegen(node):
    if node in successor_list:
        return successor_list[node]
    return []

def heuristic(node):
    return node[1]

def hill_climbing(start):
    global closed
    node = start
    print("\nStart:", node)
    
    child = movegen(node)
    child.sort(key=lambda x: x[1])
    print("Sorted Child list:", child)

    closed.append(node)

    if not child:
        print("\nNo children to expand.")
        return closed

    newNode = child[0]
    print("Initial best child:", newNode)

    while heuristic(node) > heuristic(newNode):
        print("\n------------------------------")
        node = newNode
        print("Current Node:", node)
        closed.append(node)

        child = movegen(node)
        if not child:
            print("\nNo more children")
            break

        child.sort(key=lambda x: x[1])
        print("Sorted Child list:", child)
        newNode = child[0]

    print("\nFinal CLOSED list:", closed)
    return closed

# Run
Start = ('A', 5)
hill_climbing(Start)



successor_list = {
    ('A', 5): [('B', 2), ('C', 4)],
    ('B', 2): [('D', 2), ('E', 3)],
    ('C', 4): [('F', 2), ('G', 4)],
    ('D', 2): [('H', 1), ('I', 99)],
    ('F', 2): [('J', 99)],
    ('G', 4): [('K', 99), ('L', 3)]
}


closed = []
def movegen(node):
    if node in successor_list:
        return successor_list[node]
    return []

def heuristic(node):
    return node[1]

def hill_climbing(start):
    global closed
    node=start
    print("\n Start Node:",node)
    child=movegen(node)
    if not child:
        print("\n No children to explore")
        return closed 
    
    child.sort(key=lambda x:x[1])
    print("sorted child list:",child)
    closed.append(node)
    newNode=child[0]

    while heuristic(node)>heuristic(newNode):
        print("\n------------------------------")
        node=newNode
        print("New Node:",node)
        child=movegen(node)
        if not child:
            print("\n No children found")
            break
        child.sort(key=lambda x:x[1])
        print("sorted child List:",child)
        newNode=child[0]
        closed.append(node)
        print("\n Final Closed List:",closed)
        return closed 
    


Start=('A',5)
print(hill_climbing(Start))    
