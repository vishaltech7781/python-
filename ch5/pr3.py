s = set()

s.add (18)
s.add("18")
print (s)

#both the 18 wiill be printed b'coz 18 as an integer and string are totally different from each other

se = set()
se.add(20)
se.add(20.0)
se.add('20')

print (len(se))
#here 20 and 20.0 are both same coz python only see are they numerically equal 
print( 20 == 20.0)      #expalination
