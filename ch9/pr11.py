with open("this_copy.txt")as f:
    content = f.read()

with open ("renamed_file.txt","w")as f:
    f.write(content)
