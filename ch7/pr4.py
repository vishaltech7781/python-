n = int (input("enter the number :"))

for i in range(2,n):
    if(n%i==0):
        print("the entered number is not a prime number  ")
        break;

else:
    print("entered number is a prime nummber ")