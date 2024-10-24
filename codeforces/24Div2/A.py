def main():
    n=int(input())
    
    graph={}
    
    actualGraph={}
    for i in range(n):
        graph[i]=[]
        actualGraph[i]=[]
            
    for _ in range(n):
        l=list(int(x)-1 for x in input().split())
        
        graph[l[0]].append([l[1],l[2]+1])
        graph[l[1]].append([l[0],l[2]+1])
        actualGraph[l[0]].append([l[1],l[2]])
    
    visited=[False]*n
    
    path=[-1]*n
    
    def dfs(current, visited, initial,counter):
        
        #print(path)
        if current==initial and counter>0:
            return
        
        visited[current]=True
        path[counter]=current
        # counter+=1
        
        # if current==initial and counter>0:
        #     return
        
        for neighbour in graph[current]:
            if not visited[neighbour[0]]:
                dfs(neighbour[0], visited, initial,counter+1)
                
    # ##print(path)
    
    
    dfs(0, visited, 0, 0)
    # ##print(path)
    
    lrCost=0
    rlCost=0
    
    for i in range(n):

        # x=actualGraph.get(path[i])
        
        currentNode=path[i]
        next=path[(i+1)%n]

        bidirectional=graph[currentNode]
        cost=-1
        for value in bidirectional:
            if value[0]==next:
                cost=value[1]
                break
            
        forward=False
        
        data=actualGraph.get(currentNode)
        
        if data:
            for value in data:
                if value[0]==next:
                    forward=True
                    break
                
        if forward:
            lrCost+=cost
        else:
            rlCost+=cost
            
    print(min(lrCost,rlCost))
    
        

            
        

    
# main()
                
      
def main2():
    n = int(input())  # Number of cities (and roads)
    
    clockwise_cost = 0
    counterclockwise_cost = 0
    
    roads = []
    
    for _ in range(n):
        a, b, c = map(int, input().split())  # Road from city a to city b with redirection cost c
        roads.append((a - 1, b - 1, c))      # Store roads in 0-indexed format
    
    for a, b, c in roads:
        if (b - a == 1) or (a == n - 1 and b == 0):  # Clockwise road (next city in order)
            counterclockwise_cost += c  # We need to redirect this to be counterclockwise
        else:  # Counterclockwise road
            clockwise_cost += c  # We need to redirect this to be clockwise
    
    # Minimum cost to make either clockwise or counterclockwise cycle
    print(min(clockwise_cost, counterclockwise_cost))

main2()

#####chat gpt failed the same question
  
                

    
    
        
        
    
    