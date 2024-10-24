def main():
    n=int(input())
    
    l=list(int(x)-1 for x in input().split())
    
    global visited
    visited=[False]*n

    graph={}
    
    for i in range(n):
        graph[i]=[l[i]]
    

    
    def dfs(current, visited, length, original):
        
        # if found==True:
            # return True
        
        visited[current]=True
        
        count=0
        for neighbour in graph[current]:
            if neighbour==original and length==3:
                # print("YES")
                # found=True
                return True
            elif not visited[neighbour] and length<4:
                count+=1
                if dfs(neighbour, visited, length+1, original):
                    return True
                
                
        visited[current]=False
        
        return False
        # if count==0:
            # length-=1
            # visited[current]=False
                
    
                  
    
    for i in range(n):
        visited=[False]*n
        if dfs(i,visited, 1,i)==True:
            print('YES')
            return
        
    print('NO')
        
main()