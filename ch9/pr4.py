word = "donkey"

with open("file1.txt", "r") as f:
    content= f.read()

contentnew = content.replace(word,"######")

with open ("file1.txt", "w") as f:
    f.write(contentnew)