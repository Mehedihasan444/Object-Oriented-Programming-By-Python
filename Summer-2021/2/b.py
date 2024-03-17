lis=[]
for i in range(20,61):
    if i%2==0 or i%5==0:
        if i%2==0:
           i+=5
        if i%5==0:
            i+=2
        lis.append(i)
print(lis)