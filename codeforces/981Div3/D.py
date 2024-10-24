def main():
    
    cases=int(input())
    
    
    for _ in range(cases):
        n=int(input())
        
        
        l=list(int(x) for x in input().split())
        
        

        sumIndicies = {}
        current_sum = 0
        
        found = []
        sumIndicies[0] = -1

        for i in range(n):
            current_sum += l[i]

            # Check if the curr
            if current_sum in sumIndicies:
                start_index = sumIndicies[current_sum] + 1
                found.append([start_index, i])
            sumIndicies[current_sum] = i
                
        
        # for start in range(n):
            # for end in range(start, n-start):
    
        # found=[]
    
        # for i in range(n):
        #     sum=0
        #     for j in range(i,n):
        #         sum+=l[j]
        #         if sum==0:
        #             found.append([i,j])
                    
        # print(found)
        
        
        total=0
        mine=[]
        highest=-1
        counter=0
        found.sort(key=lambda x:(x[1]))
        
        for i in range(len(found)):
            
            if found[counter][1]>highest and found[counter][0]>highest:
                total+=1
                highest=found[counter][1]
                # print(found[counter])
            counter+=1
        print(total)
        
                
                
    
    
main()