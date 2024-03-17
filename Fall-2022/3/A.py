def calculate_amount(plan:int):
    amount=0.00
    if plan==1:
        amount= 9.99
    elif plan==2:
        amount= 15.99
    elif plan==3:
        amount= 19.99
    return amount

store= dict()
i=1
while True:
    print("""
0. Exit
1. Inter info     
""")
    info=dict()
    choice=int(input("Enter Your choice number: "))
    if choice==0:
        print(store)
        exit()
    elif choice==1:
        print("If you want to exit enter 0")
        name=input("Enter Your Name: ")
        print("""
            1. Basic
            2. Standard
            3. Premium    
            """)
        plan=int(input("Choose a plan number: "))
        info["name"]=name
        if plan==1:
            info["plan"]= "Basic"
        elif plan==2:
            info["plan"]= "Standard"
        elif plan==3:
            info["plan"]= "Premium"
        info["payment"]=f"$ {calculate_amount(plan)}"
        store[i]=info
        i+=1


