
import math
def main():
    cases=int(input())
    
    
    for _ in range(cases):
        I,A=list(int(x) for x in input().split())
        
        if I>=A:
            print(I)
        else:
            print(max(0,
                      math.floor(I-math.ceil((A-I)))))
    
    
main()