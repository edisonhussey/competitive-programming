# def main():
    
#     cases=int(input())

#     for _ in range(cases):
#         n,target=list(int(x) for x in input().split())
#         l=list(int(x) for x in input().split())    

#         l.sort()
#         containers=[[0,0,0]]*n
        
#         containerPointer=0
#         count=0
#         current=l[0]
#         for i in range(n):
#             if l[i]==current:
                
#                 count+=1
#                 # if i==n-1:
#                     # containers[containerPointer]=[current,count,0]
                    
#             else:
#                 containers[containerPointer]=[current,count,0]
#                 containerPointer+=1
#                 count=1
#                 current=l[i]
#                 # if i==n-1:
#                     # containers[containerPointer]=[current,count,0]
#             if i==n-1:
#                 containers[containerPointer]=[current,count,0]                    


#         # print(containers)
        
#         for i in range(1,len(containers)):
#             # if type(containers[i])!=int:
#                 # print(containers[i])
                
#             try:
#                 containers[i][2]=containers[i][0]-containers[i-1][0]
#             except:
#                 pass

#         # print(containers)   
#         containers[0][2]=containers[0][0]
        
#         baseLength=n
        
#         checks=0
#         removed=0
        
#         for i in range(n):
#             canRemove=containers[i][2]*baseLength
#             # print(canRemove)
#             if removed+canRemove>=target:
#                 checks+=target-removed
#                 break
                
#             else:
#                 checks+=containers[i][1]
#                 removed+=canRemove
#                 checks+=canRemove
#                 baseLength-=containers[i][2]
                
#             # print("checks",checks,"removed: ",removed)
                
            
#         print(checks)
            

      
    
    
# main()


def main():
    cases = int(input())

    for _ in range(cases):
        # Read number of elements and target value
        n, target = map(int, input().split())
        l = list(map(int, input().split()))

        # Sort the list
        l.sort()

        # Create containers for unique numbers, counts, and the difference to previous
        containers = [[0, 0, 0] for _ in range(n)]

        containerPointer = 0
        count = 1
        current = l[0]

        # Loop through the list to populate containers with unique numbers and counts
        for i in range(1, n):
            if l[i] == current:
                count += 1
            else:
                containers[containerPointer] = [current, count, 0]
                containerPointer += 1
                current = l[i]
                count = 1

            if i == n - 1:
                containers[containerPointer] = [current, count, 0]

        # Final container for the last element
        containers[containerPointer] = [current, count, 0]

        # Calculate the differences between consecutive unique numbers
        for i in range(1, containerPointer + 1):
            containers[i][2] = containers[i][0] - containers[i - 1][0]

        # Set the first container's difference to its own value
        containers[0][2] = containers[0][0]

        baseLength = n
        checks = 0
        removed = 0

        # Loop through containers to calculate minimum operations needed
        for i in range(containerPointer + 1):
            canRemove = containers[i][2] * baseLength

            if removed + canRemove >= target:
                checks += target - removed
                break
            else:
                checks += containers[i][1]
                removed += canRemove
                checks += canRemove
                baseLength -= containers[i][1]

        # Output the total number of checks
        print(checks)


main()
