def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)
n = float(input("enter the number for pattern :"))
pattern(n)   