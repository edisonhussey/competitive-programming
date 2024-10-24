def main():
    n,k=list(int(x) for x in input().split())
    
    oCount=0
    # eCount=0
    if n%2==0:
        oCount=n//2
        
    else:
        oCount=n//2+1
        # eCount=n//2
        
    if k<=oCount:
        print(k*2-1)
    else:
        k-=oCount
        print(2*k)        
    # counter=0
    # for i in range(1,n+1):
    #     if i%2==1:
    #         nk[counter]=i
    #         counter+=1
            
    # for i in range(1,n+1):
    #     if i%2==0:
    #         nk[counter]=i
    #         counter+=1
            
    # print(nk[k-1])
            
    
            
    
main()