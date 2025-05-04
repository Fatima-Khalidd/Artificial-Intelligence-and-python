from pyamaze import maze, agent
from queue import PriorityQueue

def heuristic(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance

def a_star(m):
    start = (m.rows, m.cols)
    goal = (1, 1)

    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = heuristic(start, goal)

    my_open_list = PriorityQueue()
    my_open_list.put((f_score[start], heuristic(start, goal), start))

    came_from = {}  # To track the path

    while not my_open_list.empty():
        currCell = my_open_list.get()[2]

        if currCell == goal:  # If we have reached the goal
            path = []
            while currCell != start:
                path.append(currCell)
                currCell = came_from[currCell]
            path.append(start)
            path.reverse()  # Reverse the path to start from the beginning
            return path  # Return the path

        for key in 'ESNW':
            if m.maze_map[currCell][key] == True:  # If we can move in this direction
                if key == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif key == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif key == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif key == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + heuristic(childCell, goal)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    my_open_list.put((temp_f_score, heuristic(start, goal), childCell))
                    came_from[childCell] = currCell  # Track the parent cell

    return None  # If no path is found

# Main code
m = maze(10,10)
m.CreateMaze()

path = a_star(m)

if path:
    # Trace the path on the maze
    a = agent(m, footprints=True)
    m.tracePath({a: path})  # Pass the path to trace
    m.run()
else:
    print("No path found.")

print(path)  # Print the path
