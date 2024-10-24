import sys
sys.setrecursionlimit(100000)

def main():
    nodeCount, edgeCount, minLength=list(int(x) for x in input().split())
    
    graph={}
    
    for i in range(nodeCount):
        graph[i]=[]
    
    
    for _ in range(edgeCount):
        l=list(int(x) for x in input().split())

        graph[l[0]-1].append(l[1]-1)
        graph[l[1]-1].append(l[0]-1)
        
    
    path=[-1]*nodeCount
    
    
    # print(graph)
    def dfs(current, visited, length, original):
        
        # print(path)
        visited[current]=True
        path[length]=current
        # print(minLength,length)
        
        # if current==original and length>minLength:
        #     print(length)
        #     print(path[:length])
        #     return True
        

        for neighbour in graph[current]:
            
            
            if neighbour==original and length>=minLength:
                print(length+1)
                gg=list(str(x+1) for x in path[:length+1])
                # xd="".join(path[:length+1])
                print(" ".join(gg))
                return True
            
            elif not visited[neighbour]:
                if dfs(neighbour, visited, length+1, original):
                    return True
                
                
        
        visited[current]=False
        return False
                
    
    for i in range(nodeCount):
        visited=[False]*nodeCount
        if dfs(i, visited, 0, i):
            return
        
    print()
        
        
        
    
    
    
main()