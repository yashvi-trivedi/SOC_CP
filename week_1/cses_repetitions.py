string=input()
ans=1
count=1
for i  in range(1, len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        count=1
    ans=max(ans, count)

print(ans)