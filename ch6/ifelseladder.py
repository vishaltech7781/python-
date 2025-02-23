a = int(input("enter the age to be checked for eligiblity :"))

if ( a > 18):
    print("u r eligible for driving ")
    
elif (a<0):
    print("u r entering the invalid age ")

elif ( a == 0 ) :
    print("u have entered the 0 which is also invalid ")

else :
    print("u r not elgible for the driving ")    