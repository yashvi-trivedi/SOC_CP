for i in range(5):
    str_row=input().split()
    if '1' in str_row:
        x_pos=str_row.index('1')
        y_pos=i
        xdiff=abs(2-x_pos)
        ydiff=abs(2-y_pos)
        answer=xdiff+ydiff
        break
print(answer)



















'''i=0
found=False
while i<5 and found==False:
    #read a row
    str_row=input().split()
    for val in str_row:
        if val=='1':
            found=True
            x_pos=str_row.index('1')
            y_pos=i
            break
    i+=1

answer=x_pos+y_pos
print(answer)'''