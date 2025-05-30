k=int(input())
arr=[]
str_arr=input().split()
for i in range(k):
    arr.append(int(str_arr[i]))

diff=0
for j in range(1,k):
    if arr[j]<arr[j-1]:
        diff=arr[j-1]-arr[j]+diff
        arr[j]=arr[j-1]

print(diff)