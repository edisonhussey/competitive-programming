def main():
    n,x=list(int(x) for x in input().split())
    
    print(n,x)
    
    if(2**(n-1)>x):
        print('impossible')
    else:
        array=[]
        
        array.append(x-pow(2,n-1)-1)
        for i in range(n-1):
            array.append(1)

        print(array)
    
main()