def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    return a/b
while True:
    print("what would you like to do today?")
    print("click 1 to add")
    print("click 2 to subtract")
    print("click 3 to multiply")
    print("click 4 to divide")
    print("click 5 to exit")
    try:
        choice=int(input("enter choice from 1-5:"))
    except ValueError:
        print("enter valid choice")
        continue
    if choice in [1,2,3,4]:
        try:
            a=float(input("enter first number:"))
            b=float(input("enter second number:"))
            if choice==1:
                print(add(a,b))
            elif choice==2:
                print(subtract(a,b))
            elif choice==3:
                print(multiply(a,b))
            elif choice==4:
                print(divide(a,b))
        except ValueError:
            print("enter valid number")
    elif choice==5:
        print("bye!")
        break
    else:
        print("enter valid choice")
