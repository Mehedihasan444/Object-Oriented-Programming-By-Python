odd_list=[]
n=int(input("How many numbers you want to enter? "))
i=0
while True:
    if i==n:
        print(odd_list)
        break
    odd_number=int(input("Enter an odd number: "))
    odd_list.append(odd_number)
    i+=1