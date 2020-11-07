t= int(input("Enter the number of test cases: "))
for x in range(0,t):
    cp=int(input("Enter cost price "))
    sp=int(input("Enter the selling price "))
    if(cp>sp):
        print("Loss")
    elif(sp>cp):
        print("Profit")
    else:
        print("Neither")


