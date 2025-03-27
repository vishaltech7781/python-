with open ("log.txt","r") as f :
    lines = f.readlines()

lineno = 1 
for line in lines :
    if ("python" in  line ):
        print (f" yes python is persent in the log file. in line {lineno}")
        break 
    
    lineno += 1
else:
    print ("not present in log file.")


