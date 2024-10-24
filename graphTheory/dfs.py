# def dfs(currentNode,graph,parent: None):
#     print(currentNode)
    
#     # if graph[currentNode]==parent:
#         # return
        
#     if graph[currentNode]==[]:
#         return

#     for neighbour in graph[currentNode]:
#         # print(neighbour)
        
#         if neighbour!=parent:
            
#             dfs(neighbour, graph, currentNode)


# def main():
    
#     # graph = {
#     # 0: [1, 2],
#     # 1: [0, 3],
#     # 2: [0, 3],
#     # 3: [1, 2, 4],
#     # 4: [3]
#     # }
    
    
#     graph = {
#     0: [1, 2],
#     1: [ 3, 4],
#     2: [4,3],
#     3: [],
#     4: []
#     # 3: [1],
#     # 4: [1]
# }

#     dfs(0, graph, None)

# main()
import copy
    
graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [0, 3, 4],  # Node 1 is connected to nodes 0, 3, and 4
    2: [0, 4, 3],  # Node 2 is connected to nodes 0, 4, and 3
    3: [1, 2],  # Node 3 is connected to nodes 1 and 2
    4: [1, 2]   # Node 4 is connected to nodes 1 and 2          
    }
    
def dfs(current, visited, newVisited=None):
    print(current)
    # if newVisited is not None:
        # visited[newVisited]=True

    newVisited=visited.copy()
    newVisited[current]=True
    
    
    counter=0
    for neighbour in graph[current]:
        if newVisited[neighbour]==False:

            dfs(neighbour, newVisited, current)
            counter+=1
    if counter==0:
        print("\n")
            
            
# visited=[False, False,False,False,False]
# dfs(0,visited, 0)

# def main():
    
#     found=[]
    
#     graph = {
#     0: [1, 2],  # Node 0 is connected to nodes 1 and 2
#     1: [0, 3, 4],  # Node 1 is connected to nodes 0, 3, and 4
#     2: [0, 4, 3],  # Node 2 is connected to nodes 0, 4, and 3
#     3: [1, 2],  # Node 3 is connected to nodes 1 and 2
#     4: [1, 2]   # Node 4 is connected to nodes 1 and 2
# }
    
#     n=100
#     data={
#         "length": 0,
#         "path": [0]*n,
#         "root":0
#     }
#     def dfs(current, visited, data):
#         global found

#         visited[current]=1
#         data["path"][data["length"]]=current
#         data["length"]+=1
        
        
#         count=0
#         for neighbour in graph[current]:
#             if not visited[neighbour]:
#                 # data["path"][data["length"]+1]=
#                 # data["length"]+=1
#                 # data["path"][data["length"]]=neighbour
#                 count+=1
#                 dfs(neighbour, visited, data)


#         if count==0:
#             found.append(copy.copy(data["path"][:data["length"]]))
#             print(data["path"])
            
#             data["length"]-=1
#             return 
#             # data["path"][data["length"]]=0
            
            

            
#     dfs(0, [0]*100, data)
#     print(found)

# main()


import copy  # Import the copy module

def main():
    global found  # Declare found as global to access it inside dfs
    
    found = []  # Initialize the found list
    
    graph = {
        0: [1, 2],  # Node 0 is connected to nodes 1 and 2
        1: [0, 3, 4],  # Node 1 is connected to nodes 0, 3, and 4
        2: [0, 4, 3],  # Node 2 is connected to nodes 0, 4, and 3
        3: [1, 2],  # Node 3 is connected to nodes 1 and 2
        4: [1, 2]   # Node 4 is connected to nodes 1 and 2
    }
    
    n = 100  # Maximum number of nodes
    data = {
        "length": 0,  # Current length of the path
        "path": [0] * n,  # Initialize the path list with zeros
        "root": 0  # Starting node (root)
    }
    
    def dfs(current, visited, data,root):
        visited[current] = 1  # Mark the current node as visited
        data["path"][data["length"]] = current  # Add current node to the path
        data["length"] += 1  # Increment the length of the path
        
        count = 0  # Initialize count of neighbours visited
        for neighbour in graph[current]:
            if not visited[neighbour]:  # If neighbour hasn't been visited
                count += 1
                dfs(neighbour, visited, data,root)  # Recursive DFS call
            elif neighbour==root:
                print("Found a cycle: ", data["path"][:data["length"]])
            

        if count == 0:  # If no neighbours were visited
            found.append(copy.copy(data["path"][:data["length"]]))  # Store a copy of the path
            print("Current path:", data["path"][:data["length"]])  # Print the current path

        data["length"] -= 1  # Backtrack by decrementing the length
        visited[current] = 0  # Mark current node as unvisited for other paths

    # Start DFS from the root node
    dfs(0, [0] * 100, data,0)  # Initialize visited list with zeros
    print("All found paths:", found)  # Print all found paths

main()
