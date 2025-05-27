k=int(input())
i=0
string=input().split()
arr=[]
while i<k:
    arr.append(int(string[i]))
    i+=1
 
#k=7
#arr=[33, 44, 11, 22]
#arr=[10, 10, 58, 31, 63, 40, 76]
#pushing max up down
highest=max(arr)
move_max=arr.index(highest)
arr.remove(highest)
arr.insert(0, highest)
#print(f"array:{arr}")
#pulling min up
j=k-1
smallest=min(arr)
while j>=0:
    if arr[j]==smallest:
        #print(f"j: {j}")
        min_move=k-j-1
        break
    else:
        j-=1

#print(f"maxmove: {move_max}")
#print(f"minmove: {min_move}")
answer=min_move+move_max
print(answer)
