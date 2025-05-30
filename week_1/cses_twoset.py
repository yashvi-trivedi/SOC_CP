n=int(input())
S= n*(n+1)//2
target=S/2
if S%2!=0:
    print('NO')
else:
    print('YES')
    A=[]
    B=[]
    for i in range(n,0,-1):
        if target-i>=0:
            A.append(i)
            target-=i
        else:
            B.append(i)
    #A.sort()
    #B.sort()
    def convert(lst):
        
        return ' '.join(lst)

    resultA = ' '.join(map(str, A))
    print(len(A))
    print(resultA)
    resultB = ' '.join(map(str, B))
    print(len(B))
    print(resultB)