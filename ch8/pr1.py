a = int(input("enter the number: "))
b = int(input("enter the number: "))
c = int(input("enter the number: "))

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"a is the greatest of 3 numbers :{a} ")

    elif(b>a and b>c):
        print(f"b is the greatest of 3 numbers :{b}")

    else:
        print(f"c is the greatest of 3 numbers :{c} ")

greatest(a,b,c)
