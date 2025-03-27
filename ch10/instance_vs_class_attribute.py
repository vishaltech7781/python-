class Emp:
    # name = "vishal"   
    salary= 1000000 #this is class attribute
    id = 107
    language = "py"

vishal = Emp()
vishal.name = "vishal"  #this is object attribute
vishal.language = "javascript"
print(vishal.name ,vishal.salary,vishal.id,vishal.language) 
