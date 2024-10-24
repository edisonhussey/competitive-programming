def main():
    
    s=input()
    s2=input()
    
    # s2.__reversed__()
    
    
    
    
    # print(s,s2)
    if len(s)==len(s2):
        for i in range(len(s)):
            # print(s[i],s2[i])
            if s[i]!=s2[len(s)-i-1]:
                return 'NO'
            
        return 'YES'
    else:
        # print('NO')
        return 'NO'
print(main())