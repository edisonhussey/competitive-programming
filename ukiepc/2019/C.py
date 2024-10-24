

import heapq

# Create an empty list to represent the heap
priority_queue = []

# Input the size of the list and the value of k
l0 = list(int(x) for x in input().split())
n = l0[0]  # Size of the list
k = l0[1]  # Not used in this example

# Input the list of numbers
l2 = list(int(x) for x in input().split())

# Create a container to count occurrences
container = {}

# Count occurrences of each value
for value in l2:
    if container.get(value) is not None:
        container[value] += 1
    else:
        container[value] = 1
        
# Add the values and their counts as tuples (key, value) to the priority queue
for key, value in container.items():
    heapq.heappush(priority_queue, (-value, key))

# print(priority_queue)

hands=[]    

while True:
    currentHand=[]
    counter=k
    outcome=True
    found={}
    
    toPushBack=[]
    while counter and priority_queue:
        key,value=heapq.heappop(priority_queue)
        if found.get(value):
            # toPushBack((key,value))
            toPushBack.append([key,value])
            
        else:
            if key==0:
                pass
            else:
                currentHand.append(value)
                # toPushBack(key-1,value)
                toPushBack.append([key+1,value])
                counter-=1
                found[value]=1
                
    for value in toPushBack:
        heapq.heappush(priority_queue,(value[0],value[1]))
        
    # print(priority_queue)
    # print(currentHand)
        
        
    if len(currentHand)<k:
        break
    else:
        hands.append(currentHand)
        # print(*currentHand, sep=" ")

if len(hands)==0:
    print('impossible')
else:
    for value in hands:
        print(*value, sep=" ")
        
        
                
    
                
        
                

        
            
            
        
        
