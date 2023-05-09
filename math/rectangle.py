n=4
m = n
print()
for row in range(n):
    for col in range(m):
        if  (col == 0 or col == m-1) :
            print("+",end='')
        else:
            print(end=' ')
    print()
   


