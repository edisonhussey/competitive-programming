
# def sortCustom(array):
    
def sort(array):
    
    array.sort(key=lambda x:(x[0]+x[1]))
    return array

# print(sort([1,200],[12]))

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            pointer=0
            a0=array[i][0]
            a1=array[i][1]
            
            b0=array[j][0]
            b1=array[j][1]
            
            if b0>a0:
                pointer+=1
            elif a0>b0:
                pointer-=1
                
            if b1>a0:
                pointer+=1
            elif a0>b1:
                pointer-=1
                
                
            if b0>a1:
                pointer+=1
            elif a1>b0:
                pointer-=1
                
            if b1>a1:
                pointer+=1
            elif a1>b1:
                pointer-=1
                
            if pointer<0:
                array[i],array[j]=array[j],array[i]
                
            
            
            

    return(array)

# print(sort([[3,2],[4,3],[2,1]]))            
# print(sort([[5,10],[2,3],[9,6],[4,1],[8,7]]))                        
# print(sort([[1,200],[12,12]]))
    
    
    
def main():
    
    
    cases=int(input())
    
    for _ in range(cases):
        n=int(input())
        
        array=[0]*n
        
        
        for i in range(n):
            l=list(int(x)for x in input().split())
            array[i]=l
            
        array=sort(array)
        
        new=[0]*(2*n)
        pointer=0
        for value in array:
            new[pointer]=str(value[0])
            pointer+=1
            
            new[pointer]=str(value[1])
            pointer+=1
            
        val=" ".join(new)
        
        print(val)
            
            
            
        
            
        
            
    
    
main()