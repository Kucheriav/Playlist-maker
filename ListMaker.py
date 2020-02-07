#123.py
import os
import random
def imaginary_files():
    n = random.randint(1,10)
    x = ['a','b','c','d','e','f','g','h']
    file_list = []
    for i in range(n):
        file_list.append([])
        for j in range(random.randint(1,len(x))):
            file_list[i].append(random.choice(x))
    return file_list
                    
def make_file_lists():   
    home = os.getcwd()
    folders = os.listdir()
    folders.remove('123.py')
    file_lists= []
    for folder in folders:
        os.chdir(home+'\\'+folder)
        file_lists.append(os.listdir())
        os.chdir(home)
    return file_lists

file_lists =imaginary_files()
#file_lists = make_file_lists()
result ={}
for file_list in file_lists:
    for file in file_list:
        if file not in result:
            result[file] = 1
        else:
            result[file] += 1
list_d = list(result.items())
list_d.sort(key=lambda i: i[1])

list_d.reverse()
        
