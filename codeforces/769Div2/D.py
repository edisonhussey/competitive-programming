def gcd(a,b):
    if b>a:
        a,b=b,a
        
    r=-1
    # a,b,r   40,25
    # r=a%b
    while r!=0:
        r=a%b
        a,b=b,r
        
    return a



def main():
    n=int(input())
    array=list(int(x) for x in input().split())
    
    # array.reverse()
    best=[]
    bestValue=0
    
        
    for i in range(n):
        best.append(-1)
        
    # print(array)
        
    toConsider=[]
    
    for i in range(n):
        if toConsider:
            # print('f')
            outcome=True
            for j in range(len(toConsider)):
                toConsider[j]=gcd(toConsider[j],array[i])
                
                print(toConsider[j],len(toConsider)+1-j)
                if(toConsider[j]==len(toConsider)+1-j):
                    outcome=False
                    break
            if outcome==True:
                toConsider.append(array[i])
                best[i]=bestValue
            else:
                bestValue+=1
                best[i]=bestValue
                toConsider=[array[i]]
                    
        else:

            if array[i]==1:
                bestValue+=1
                best[i]=bestValue
            else:
                toConsider=[array[i]]
                best[i]=bestValue
    
    print(best,toConsider)            
    
    
    
    
main()