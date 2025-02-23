age = int (input("enter the age to be checked for the validation of the driving : "))

if (age % 2 == 0) :{
    print( " entered number is even ")
}
if ( age %2 == 1):{
    print( " entered number is odd ")
}   
if ( age >=18): {
    print(" u r elegible for driving as per ur age ")
}    
elif( age <0 ):{
    print(" entered age is negative number which can't be an age enter the valid age ")
}    
elif ( age == 0):{
    print("entered is age is 0 which cant be age as per living being ")
}
else :{
    print("enter the valid age for validation for driving eligiblity")
}
