dict = {}   #empty dictionary
a ={
    "vishal":100,
    "aditya":20,
     "yash":99
}
print(type(a))
print(a.items())
print(a.keys())
print (a.values())
a.update({"vishal":101,"yash":100,"aditya":10})
print(a.items())
print(a.get("vinay"))
#print(a["vinnay"])   
print(a.pop("aditya"))   
print(a.items())

