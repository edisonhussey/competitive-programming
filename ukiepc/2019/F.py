import math
def main():
    
    l0=list(int(x) for x in input().split())
    n=l0[0]
    c=l0[1]
    
    
    l1=list(int(x) for x in input().split())
    
    l1.sort()
    
    answer=0
    left=0
    right=None
    
    for i in range(n):
        if l1[n-i-1]+l1[0]<=c:
            right=n-i-1
            break
        
    if right is not None:
        answer+=math.ceil(right-left/2)
        answer+=n-1-right
        
    else:
        answer=n
        
    print(answer)
        
    
    
        
    
    
    
    
    
    
main()