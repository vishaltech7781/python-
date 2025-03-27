with open ("log.txt","r") as f :
    content = f.read()

if ("python" in  content):
    print (" yes python is persent in the log file.")
else :
    print ("not present in log file.")