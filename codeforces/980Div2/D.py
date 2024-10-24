import math
from collections import defaultdict
def main():
    cases=int(input())
    
    for _ in range(cases):
        n=int(input())
        scores=list(int(x) for x in input().split())
        pointers=list(int(x)-1 for x in input().split())
        minimizingCost=[0]*n
        sumUpTo=[0]*n
        init=0
        
        if n==1:
            print(scores[0])
            continue
        
        # pointerToOriginal={}
        pointerToIndex=defaultdict(list)
        for i in range(n):
            init+=scores[i]
            
            # case2(init,i,sumUpTo)
            sumUpTo[i]=init
            
            currentPointer=pointers[i]
            pointerToIndex[currentPointer].append(i)
        
        #print('pointer to index: ', pointerToIndex)
                    
        for i in range(1,n):
            best=math.inf
            #print("pointer to index: ",pointerToIndex[i])
            #print("minimizing cost: ",minimizingCost)
            
            for value in pointerToIndex[i]:
                if minimizingCost[value]<math.inf and value<i:
                    if scores[value]+minimizingCost[value]<best:
                        best=scores[value]+minimizingCost[value]
                        
            minimizingCost[i]=best
        #print(minimizingCost)
        
        
        #print("best array is: ", minimizingCost)
        for i in range(n-1):
            index=n-i-2
            #print(index,"value of index")
            left=minimizingCost[index]
            right=minimizingCost[index+1]
            #print(left,right,min(left,right))
            minimizingCost[index]=min(left,right)
            # minimizingCost[index]=min(minimizingCost[index],minimizingCost[index+1])
            
        #print(minimizingCost)
        
        for i in range(1,n):
            best=minimizingCost[i]
            #print("pointer to index: ",pointerToIndex[i])
            #print("minimizing cost: ",minimizingCost)
            
            for value in pointerToIndex[i]:
                if minimizingCost[value]<math.inf and value<i:
                    if scores[value]+minimizingCost[value]<best:
                        best=scores[value]+minimizingCost[value]
                        
            minimizingCost[i]=best
        #print(minimizingCost)
            
        bestConsider=0      
        for i in range(n):
            consider=sumUpTo[i]-minimizingCost[i]
            if consider>bestConsider:
                bestConsider=consider
        print(bestConsider)
        
                    
