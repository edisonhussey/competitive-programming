import math
def main():
    
    cases=int(input())
    
    for _ in range(cases):
        n=int(input())
        l=list(int(x) for x in input().split())
        
        
        if n==1:
            print(0)
            continue
        
        
        elif n%2==0:
            
            originalBest=[math.inf]*(n//2)
            reverseBest=[math.inf]*(n//2)
            
            originalBest[0]=0
            reverseBest[0]=0
            
            for i in range(1,n//2):
                left=i
                right=n-1-i
                
                o0=originalBest[i-1]
                o1=reverseBest[i-1]
                
                if l[left]==l[left-1]:
                    o0+=1
                if l[right]==l[right+1]:
                    o0+=1
                    
                if l[left]==l[right+1]:
                    o1+=1
                    
                if l[right]==l[left-1]:
                    o1+=1
                    
                originalBest[i]=min(o0,o1)
                
                r0=originalBest[i-1]
                r1=reverseBest[i-1]
                
                if l[right]==l[left-1]:
                    r0+=1
                if l[left]==l[right+1]:
                    r0+=1
                    
                if l[right]==l[right+1]:
                    r1+=1
                    
                if l[left]==l[left-1]:
                    r1+=1

                reverseBest[i]=min(r0,r1)
                
                
                
            extra=0
            
            if l[n//2]==l[n//2-1]:
                extra=1
        
            # print(reverseBest,originalBest)
            print(min(reverseBest[-1]+extra,originalBest[-1]+extra))
            
        
        else:
            
            originalBest=[math.inf]*(n//2)
            reverseBest=[math.inf]*(n//2)
            
            originalBest[0]=0
            reverseBest[0]=0
            
            for i in range(1,n//2):
                left=i
                right=n-1-i
                
                o0=originalBest[i-1]
                o1=reverseBest[i-1]
                
                if l[left]==l[left-1]:
                    o0+=1
                if l[right]==l[right+1]:
                    o0+=1
                    
                if l[left]==l[right+1]:
                    o1+=1
                    
                if l[right]==l[left-1]:
                    o1+=1
                    
                originalBest[i]=min(o0,o1)
                
                r0=originalBest[i-1]
                r1=reverseBest[i-1]
                
                if l[right]==l[left-1]:
                    r0+=1
                if l[left]==l[right+1]:
                    r0+=1
                    
                if l[right]==l[right+1]:
                    r1+=1
                    
                if l[left]==l[left-1]:
                    r1+=1

                reverseBest[i]=min(r0,r1)
                
            extra=0
            
            if l[n//2-1]==l[n//2]:
                extra+=1
            if l[n//2+1]==l[n//2]:
                extra+=1
                
            
                
                
        
            # print(reverseBest,originalBest)
            print(min(reverseBest[-1]+extra,originalBest[-1]+extra))
            
            
            
                
                
                
                
    
    
    
main()