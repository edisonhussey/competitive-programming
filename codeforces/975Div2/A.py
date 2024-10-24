import math
def main():
    cases=int(input())
    for _ in range(cases):
        n=int(input())
        l=list(int(x) for x in input().split())
        
        
        if n==1:
            print(l[0]+1)
            continue
        b0=-1
        b1=-1
        

        #[best,countRed]

        for i in range(n):
            if i%2==0 and l[i]>b0:
                b0=l[i]
            elif i%2==1 and l[i]>b1:
                b1=l[i]
                
        print(max(b0+int(math.ceil(n/2)),b1+int(math.floor(n/2))))
                
            
        # print(max(best00[-1],best10[-1],best01[-1]))
main()
