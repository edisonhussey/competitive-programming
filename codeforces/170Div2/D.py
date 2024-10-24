# # def main():
# #     # return

# #     length, sumPoints=list(int(x) for x in input().split())
# #     l=list(int(x) for x in input().split())
    
    
    
# #     mina=[0]*length
# #     minb=[0]*length
# #     sumArray=[0]*length
    
    
# #     if l[0]!=0:
# #         return 0
# #     else:
# #         sumArray[0]=1
# #         mina[0]=0
# #         minb[0]=0
    
# #     at=0
# #     passed=1
# #     for i in range(1,length):
# #         value=l[i]
        
# #         if value>0:
# #             if value>mina[i-1]:
# #                 mina[i]=value
# #             else:
# #                 mina[i]=mina[i-1]
                
# #             minb[i]=minb[i-1]
# #             sumArray[i]=sumArray[i-1]
# #         elif value<0:
# #             if value<minb[i-1]:
# #                 minb[i]=value
# #             else:
# #                 minb[i]=minb[i-1]
                
# #             mina[i]=mina[i-1]
# #             sumArray[i]=sumArray[i-1]
            
# #         else:
# #             sumArray[i]=sumArray[i-1]+1
# #             mina[i]=mina[i-1]
# #             minb[i]=minb[i-1]


# #         if value!=0:
# #             if sumArray[i]<abs(mina[i])+abs(minb[i]):
# #                 at=i
# #                 break
# #             else:
# #                 passed+=1
                
# #         print(passed,sumArray,mina,minb)
                
# #     print(passed)
        
            
            
            

    
    
# class permutations:
    
#     def __init__(self, maximum) -> None:
#         self.a=[0]*(maximum+2)
#         self.b=[0]*(maximum+2)
        
#         self.sum=0
#         self.ablength=1
    
        
#     def increment(self):
#         print(self.a,self.b)
#         self.ablength+=1
#         self.a[self.ablength]=self.a[self.ablength-1]
#         self.b[self.ablength]=self.b[self.ablength-1]
        
#     def change(self, value):
#         if value>0:
#             for i in range(self.ablength):
#                 if i>=value:
#                     self.a[i]+=1
                    
#         elif value<0:
#             for i in range(self.ablength):
#                 if i>=abs(value):
#                     self.b[i]+=1
                    
#         else:
#             self.increment()
            
#     def __str__(self) -> str:
#         return self.a,self.b
        
    

# def main():
#     length, sumPoints=list(int(x) for x in input().split())
#     l=list(int(x) for x in input().split())
    
#     permu=permutations(sumPoints)
    
#     for i in range(length):
#         permu.change(l[i])
        
#     print(permu)
#     return 
#     # ab=[0,0]*(sumPoints+1)
#     # a=[0]*(sumPoints+2)
#     # b=[0]*(sumPoints+2)
    
#     pointer=1
#     #the sum of a+b
    
#     # if l[0]
    
#     if l[0]==0:
#         pointer+=1
    
#     for i in range(length):
        
#         # print(a,b)
#         current=l[i]
#         if current==0:
            
#             pointer+=1
            
            
#             a[pointer]=a[pointer-1]
#             b[pointer]=b[pointer-1]
            
#         # else:
                        
            
#         elif current>0:
#             # print(current,a)
            
#             for j in range(pointer):
#                 print(j,"j",current,a)
#                 if j>=current:
#                     a[j]+=1
#         else:
#             for j in range(pointer):
#                 if pointer-1-j>=abs(current):
#                     b[pointer-1-j]+=1
                    
#     print(a,b)
                    
                                
#     # print(a,b)
            
            
            
        
#         # if current[i]+=1
    
    
# main()



def main():
    n,k=list(int(x) for x in input().split())
    
    l=list(int(x) for x in input().split())
    best={(0,0):0}

    if k==0:
        print(0)
        return

    for i in range(n):
        # print(best)
        current=l[i]
        
        if current==0:
            temp={}
            for key, value in best.items():
                case1=(key[0]+1,key[1])
                case2=(key[0],key[1]+1)
                

                
                find=temp.get(case1)
                if find:
                    temp[case1]=max(value, find)
                else:
                    temp[case1]=value
                
                find2=temp.get(case2)
                if find2:
                    temp[case2]=max(value, find2)
                else:
                    temp[case2]=value
            best=temp

        elif current>0:
            # print(best, current)

            for key, value in best.items(): 
                

                if key[0]>=current:
                    best[key]+=1
                    
            # print(best, current)
                    
        elif current<0:

            for key, value in best.items():
                

                if key[1]>=abs(current):
                    best[key]+=1
                    
    # print(best)
    # bestValue=0
    # for value in best.values():
        # if value>bestValue:
            # bestValue=value
            
    print(max(best.values()))
        



                



    
main()