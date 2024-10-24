def main():
    
    
    l0=list(int(x) for x in input().split())
    # print(n,c)
    n,c=l0[0],l0[1]    
    l1=list(int(x)-1 for x in input().split())
    
    info={}
    
    array=[]
    for i in range(n-1):
        # info[i]=i
        # info[i+1]=
        array.append(i)

        
        
    # [1,2,3,4,5]
    
    #start 0 

    # info[0]=None
    for i in range(len(l1)-1):
        array[l1[i+1]]=l1[i+1]
    
    
        
        
        
   
    # value=1
    # current=0
    # for value in l1:
    for i in range(len(l1)-1):
        index=info[l1[i+1]]
        
        array[index]=l1[i+1]
        info[l1[i+1]]=None
        
    print(array)

        # if value==0:
            # continue
        # lookUp=array[value][0]

        # array[lookUp][0]=value
        # array[lookUp][1]+=1
        # temp=array[current][0]
        # array[value][0]
        # current=temp
        
    # print(array)

        
        

        
    
    
main()