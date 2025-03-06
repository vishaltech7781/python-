n = int(input("enter the number whose factorial is to be found :"))
fact =1
for i in range (1,n+1):
    fact = fact *i

print(f"factorial of the number {n} is : {fact}")