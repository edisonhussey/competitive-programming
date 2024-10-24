# import math
# def main():
    
#     def distance(a, b):
#         return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
#     lenPath=int(input())
#     path=list(int(x) for x in input().split())
    
#     stationCount=int(input())
#     stationTypes=list(int(x) for x in input().split())
    
#     stationMap={}
    
#     interval=2*math.pi/stationCount
#     angle=0

#     for i in range(stationCount):
#         if stationMap.get(stationTypes[i]) is not None:
#             stationMap[stationTypes[i]].append([math.sin(angle),math.cos(angle)])
#         else:
#             stationMap[stationTypes[i]]=[[math.sin(angle),math.cos(angle)]]
#         angle+=interval
            
    
#     # print(stationMap)
#     best=[]
#     #[[xy], value]
#     first=path[0]
#     for i in range(len(stationMap[first])):

#         best.append([stationMap[first][i], 1])
        

        
        
#     for i in range(1,lenPath):
#         targets=stationMap[path[i]]
#         newBest=[]

#         for value in targets:
#             localBest=math.inf
            
            
#             for j in range(len(best)):
#                 newDistance=best[j][1]+distance(best[j][0],value)
#                 if newDistance<localBest:
#                     localBest=newDistance
                    
#             newBest.append([value, newDistance])
            
#         best=newBest

#     afterBest=math.inf
#     # print(best)
#     for i in range(len(best)):
#         if best[i][1]<afterBest:
#             afterBest=best[i][1]
            
            
#     print(round(afterBest-1,6))                    
                
                
            
        

        
    
    
# main()

import math

def main():
    # Define the function to calculate Euclidean distance between two points on the unit circle
    def distance(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    lenPath = int(input())  # Length of the path
    path = list(int(x) for x in input().split())  # Path of stations

    stationCount = int(input())  # Total number of stations
    stationTypes = list(int(x) for x in input().split())  # Types of stations

    stationMap = {}

    # Assign coordinates to each station type on a unit circle
    interval = 2 * math.pi / stationCount  # Angle between each station
    angle = 0

    for i in range(stationCount):
        if stationMap.get(stationTypes[i]) is not None:
            stationMap[stationTypes[i]].append([math.sin(angle), math.cos(angle)])
        else:
            stationMap[stationTypes[i]] = [[math.sin(angle), math.cos(angle)]]
        angle += interval

    # Step 1: Initialize 'best' list with the coordinates of the first station in the path
    best = []
    first = path[0]
    for i in range(len(stationMap[first])):
        best.append([stationMap[first][i], 0])  # Initial cost is 0 for the first station

    # Step 2: Iterate through the rest of the path, updating the cost to visit each station
    for i in range(1, lenPath):
        targets = stationMap[path[i]]  # Stations we want to visit at step i
        newBest = []  # To store the best distances at this step

        for value in targets:
            localBest = math.inf  # Start with infinity for the minimum distance
            
            # Compare the distance from all previous stations to the current station
            for j in range(len(best)):
                newDistance = best[j][1] + distance(best[j][0], value)
                if newDistance < localBest:
                    localBest = newDistance
            
            # Append the current station and its new best distance to 'newBest'
            newBest.append([value, localBest])

        # Step 3: Update 'best' for the next iteration
        best = newBest

    # Step 4: Find the minimum distance from the last set of best distances
    afterBest = min([b[1] for b in best])

    # Step 5: Print the result, subtracting 1 for the extra initial increment in the code logic
    print(round(afterBest, 6))

main()
