'''
factorial(0)= 1
factorial(1)= 1
factorial(2)= 1x2
factorial(3)= 1x2x3
factorial(4)= 1x2x3x4
factorial(5)= 1x2x3x4x5

factorial(n)= n* n-1* ....... 3*2*1
factorial(n)= n * factorial (n-1)

'''
def fact(n):
    if(n==1 or n==0):
        return 1 
    else :
        return n*fact(n-1)

n = int(input("enter the number of which factrial is to be find :"))
print(f"factorial of the number {n} is :{fact(n)}")
# fact(n)