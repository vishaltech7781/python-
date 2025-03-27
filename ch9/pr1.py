f = open("poem.txt","r")
content = f.read()
if( "little" in content):
    print("the word little is present in the file content")

else:
    print("the word little is not present in the file content")

f.close()   