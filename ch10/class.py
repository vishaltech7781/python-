class Emp:
    # name = "vishal"   #this is class attribute
    salary= 1000000
    id = 107

vishal = Emp()
vishal.name = "vishal"  #this is object attribute
print(vishal.name ,vishal.salary,vishal.id)

yash = Emp()
yash.name= "yash"
print(yash.name,yash.salary,yash.id)

#here name is object attribute and salary and id is class attribute