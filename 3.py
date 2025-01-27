import os
# select the directory whose content u want to list
directory_path = '/'
#use the os moudle to list the directory 
contents = os.listdir(directory_path)
print(contents)