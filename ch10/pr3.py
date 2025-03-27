class demo:
    a= 4
o = demo()
print(o.a)#prints the instance attribute because object attribute is not present 
o.a = 0 #object attribute is set  
print(o.a)#print the instance attribute because it is present
print(demo.a)#class is not changed 
