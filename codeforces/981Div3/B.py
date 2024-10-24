def main():
    matrix=[]
    
    cases=int(input())
    
    
    for _ in range(cases):
        matrix=[]
        
        n=int(input())
        
        counter=0
        
        # print(matrix)
        for i in range(n):
            l=list(int(x) for x in input().split())
            matrix.append(l)
            
        # print(matrix)
            
        for i in range(n):
            smallest=1
            left=0
            right=i
            
            while 0<=left<n and 0<=right<n:
                if matrix[left][right]<smallest:
                    smallest=matrix[left][right]
                left+=1
                right+=1
                
            if smallest<0:
                counter+=abs(smallest)
            
        for i in range(1,n):
            smallest=1
            left=i
            right=0
            
            while 0<=left<n and 0<=right<n:
                if matrix[left][right]<smallest:
                    smallest=matrix[left][right]
                left+=1
                right+=1
                
            if smallest<0:
                
                counter+=abs(smallest)
            
        print(counter)
            
                
            
                    
             
    
main()
    