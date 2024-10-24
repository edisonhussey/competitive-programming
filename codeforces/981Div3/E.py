# def main():
    
#     cases=int(input())
    
    
#     for _ in range(cases):
#         n=int(input())
        
        
#         l=list(int(x)-1 for x in input().split())
        
#         fix=[False]*n
        
#         for i in range(n):
            
#             if fix[i]==False:
#                 if l[i]==i:
#                     fix[i]=True
                    
#                 elif l[l[i]]==i:
#                     fix[i]=True
#                     fix[l[i]]=True
                

#         print(fix)
        
            
    
    
# main()


def main():
    t = int(input().strip())  # Number of test cases
    results = []
    
    for _ in range(t):
        n = int(input().strip())  
        p = list(map(int, input().strip().split()))  
        
        visited = [False] * n
        total_swaps = 0
        
        for i in range(n):
            if not visited[i]:
                cycle_length = 0
                current = i
                
                while not visited[current]:
                    visited[current] = True
                    current = p[current] - 1  
                    cycle_length += 1
                

                if cycle_length >= 3:
                    total_swaps += 1
        
        results.append(str(total_swaps))
    
        print(results[-1])

main()
