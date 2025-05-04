from os import path
from pyamaze import maze,agent
from queue import PriorityQueue

def maze_ucs(m):
    start=(m.rows,m.cols)
    goal=(1,1)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0

    open_list=PriorityQueue()
    open_list.put((g_score[start],start))

    came_from={} # To track the path
    while not  open_list.empty():
        currCell=open_list.get()[1]
        if currCell==goal:
            path =[]
            while currCell!=start:
                path.append(currCell)
                currCell=came_from[currCell]
                path.append(start)
                path.reverse()
                return path
                
        for key in 'ENSW':
            if m.maze_map[currCell][key]==True:
                if key=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if key=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if key=='N':
                    childCell=(currCell[0]+1,currCell[1])
                if key=='S':
                    childCell=(currCell[0]-1,currCell[1])
                temp_g_score=g_score[currCell]+1
                if temp_g_score<g_score[childCell]:
                    g_score[childCell]=temp_g_score
                    
                return None    










m=maze(10,10) 
m.CreateMaze()
maze_ucs(m)
a=agent(m,footprints=True)
m.tracepath({a:path})
m.run()


