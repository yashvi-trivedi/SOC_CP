str_nk=input().split()
n=int(str_nk[0])
k=int(str_nk[1])
i=0
str_arr=input().split()
ans=0
for i in range(n):
    if int(str_arr[i])>=int(str_arr[k-1]) and int(str_arr[k-1])!=0:
        ans+=1
print(ans)

