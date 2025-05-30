n=int(input())
if n==1:
    print('1')
elif n<=3:
    print('NO SOLUTION')
else:
    A=[]
    B=[]
    for i in range(n, 0, -1):
        if i%2==0:
            B.append(i)
        else:
            A.append(i)

    ans=A+B
    resultA = ' '.join(map(str, ans))
    print(resultA)