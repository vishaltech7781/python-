with open("this.txt") as f :
    content1= f.read()

with open("this_copy.txt") as f :
    content2= f.read()


if (content1 == content2 ):
    print ("the content in file this is similar to content in file this_copy .")

else:
    print("content of present in the file is not similar ")