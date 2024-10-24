import math
def main():
    cases=int(input())
    
    for _ in range(cases):
        n=int(input())
        l=list(int(x) for x in input().split())

        l.sort()
        
        for i in range(n-1):
            l[i+1]=math.floor((l[i]+l[i+1])/2)
        print(l[n-1])
        
        
    
main()