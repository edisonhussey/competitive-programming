import math
def main():
    
    
    
    l0=list(int(x) for x in input().split())
    
    array=[]
    
    for _ in range(l0[0]):
        l2=list(float(x) for x in input().split())
        print(l2)

        square=l2[0]**2+l2[1]**2+l2[2]**2
        array.append(math.sqrt(square))
        

    array.sort()

    
    print(format(array[l0[1]-1],".6f"))
    
main()
