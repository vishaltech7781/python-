#  c/5 = (f-32)/9
# c= 5*(f-32)/9

def f_to_c(f):
    c=5*(f-32)/9
    print(f"conversion of farenight :{f} to degree celcius :{c} ")

f= int(input("enter the temp for farenight :"))

f_to_c(f)
