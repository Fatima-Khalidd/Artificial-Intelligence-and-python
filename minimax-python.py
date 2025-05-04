
import math

# Minimax algorithm implementation in Python
def minimax(current_depth,node_value,max_player,leaf_nodes,max_depth):
    if current_depth==max_depth:
        return leaf_nodes[node_value]
    
    if max_player:
        return max(minimax(current_depth+1,node_value*2+1,False,leaf_nodes,max_depth),minimax(current_depth+1,node_value*2+1,False,leaf_nodes,max_depth)) # 1st argument/function call = first child , 2nd argument/function call = second child. thiis how it will return max valye from the 2 children for maxplayer
    
    else:
        return min(minimax(current_depth+1,node_value*2+1,True,leaf_nodes,max_depth),minimax(current_depth+1,node_value*2+1,True,leaf_nodes,max_depth))
    

# Main function to run the minimax algorithm

leaf_nodes=[]
score=int(input("Enter numober of leaf nodes:"))
for score in range(score):
    leaf_nodes.append(int(input("Enter value of leaf node:")))

max_depth=int(math.log(len(leaf_nodes),2)) # calculating the depth of the tree
current_depth=int(input("Enter current depth of the tree:")) # prompting user to enter current depth of the tree
node_value=int(input("Enter starting node value:"))
max_player=True # starting with max player

answer=minimax(current_depth,node_value,max_player,leaf_nodes,max_depth)
print("The answer is: ",answer) 