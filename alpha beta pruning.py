#maximjum,minimum=int(input("enter value of maximum/alpha as -infinity:")),int(input("enter value of minimum/beta as +infinity:"))
beta,alpha=1000,-1000

def alpha_beta_pruning(depth,node,maxPair_value,leaf_nodes,alpha,beta,max_depth):
    # base case
    if depth==max_depth:
        return leaf_nodes[node]
    
    if maxPair_value:
        best=alpha
        for i in range(0,2):
            value=alpha_beta_pruning(depth+1,node*2+i,False,leaf_nodes,alpha,beta,max_depth) # traversing left and right child of the node
            best=max(best,value)
            alpha=max(alpha,best) # update minimum value
            if beta<alpha:
                break  # pruning the tree 
        return best # return the best value of the node
    else:
         best=beta
         for i in range(0,2):
             value=alpha_beta_pruning(depth+1,node*2+i,True,leaf_nodes,alpha,beta,max_depth)
             best=min(best,value)
             beta=min(beta,best)
             if beta<alpha:
                 break
         return best 

 

leaf_nodes=[]
score=int(input("enter the score of the leaf node: "))

for scr in range(score):
    node_value=int(input("Enter value of the node: ")) 
    leaf_nodes.append(node_value)


# prompting user to entter depth of tree
depth=int(input("Enter depth of the tree: "))
max_depth=int(input("Enter maximum depth of the tree: "))
node=int(input("Enter the node value : ")) # node from where we are starting traversing
print("Optimized value is :",alpha_beta_pruning(depth,node,True,leaf_nodes,alpha,beta,max_depth)) # calling the function to get the optimized value
