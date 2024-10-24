def main():
    x=int(input())
    
    def isDistinct(strr):
        contains={}
        for i in range(len(strr)):
            if contains.get(strr[i]):
                return False
            contains[strr[i]]=1
        return True
    
    

    for i in range(1,10000):
        if isDistinct(str(x+i)):
            print(x+i)
            break
        

    
    
    
main()