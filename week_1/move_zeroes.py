arr=[0, 1, 5, 3, 0, 21]
zer=0
m=len(arr)
notzer=0
while notzer<m:
    if arr[notzer]==0:
        del arr[notzer]
        m=len(arr)
        zer+=1
    else: 
        notzer+=1
while zer>0:
    arr.append(0)
    zer-=1
print(arr)