s = {1,3,5,7,2,4,6}

#set methods
print(len(s))
print(s.remove(3))
print(s)
print(s.clear())

s1 = { 24,34,33,22,55}
s2 = {24,55,66,33,22}

#intersection and union 
print( s1.union(s2))
print(s1.intersection(s2))

#issubset method()
print({33,22}.issubset(s1))
print({22,99}.issubset(s1))

#issuperset method()
print(s2.issuperset({24,66}))
print(s2.issuperset({22,11}))



