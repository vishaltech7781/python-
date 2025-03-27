

def remove(l,word):
    n = []
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n
l =["varry","shal","yash","aditya","sh"]        
print(remove(l,"sh"))