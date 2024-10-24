def main():
    cases=int(input())
    
    for _ in range(cases):
    
        n, toAdd=list(int(x) for x in input().split())
        l=list(int(x) for x in input().split())
        
        info={}
        
        for i in range(n):
            consider=info.get(l[i])
            if consider:
                # value=l[i]
                # count=info[consider]
                

                while True:
                    l[i]+=toAdd
                    if info.get(l[i])==None:
                        info[l[i]]=1
                        break
                    # l[i]+=toAdd
                    
                
                
            else:
                info[l[i]]=1
                
        # print(inf,)
        sorter=[]
        
        for value in info.keys():
            sorter.append(value)
        sorter.sort()
        
        found=False
        
        for i in range(len(sorter)):
            if sorter[i]!=i:

                print(i)
                found=True
                break
        if found==False:
            print(len(sorter))
        
        # print(sorter)
        # if len(sorter)==1:
        #     if sorter[0]==0:
        #         print(1)
        #     else:
        #         print(0)
        # elif sorter[0]>0:
        #     print(0)
        # else:
            
        #     found=False
        #     for j in range(len(sorter)-1):
                
        #         if sorter[j]>1+sorter[j-1]:
        #             print(sorter[j-1]+1)
        #             found=True
        #             break
            
        #     if found==False:
        #         print(sorter[-1]+1)
                
        
            
    
    
    
main()