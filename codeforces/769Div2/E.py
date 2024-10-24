class Node():
    def __init__(self, value, parent, depth) -> None:
        self.value=value
        self.parent=parent
        self.depth=depth
        self.children=[]
        
    def addChild(self, value):
        at=self.children
        while True:
            for v in at:
                if v.value==value:
                    v.addChild()
                    break
                at=v.children
                    
                

        self.children.append(Node(value, self,self.depth+1))
        

a=Node(0, None, 0)


        

def main():
    
    # cases=int(input())
    
    # for _ in range(cases):
    
    n=int(input())
    
    matrix=[]
    
    matrix={}
    
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
            
    for _ in range(n-1):
        l=list(int(x)-1 for x in input().split())
        matrix[l[0]][l[1]]=1
        
        
    root=Node(0, None, 0)    
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                # tree.addChild(j)
                return
                
        
    print(matrix)
    
        
        
    
    
    
main()