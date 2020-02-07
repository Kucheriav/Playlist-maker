#ListMaker.py
import os
import random

def make_filelists():  
    home = os.getcwd()
    folders = os.listdir()
    folders.remove('ListMaker.py')
    filelists = [] 
    for folder in folders:
        os.chdir(home+'\\'+folder)
        filelists.append(os.listdir())
        os.chdir(home)
    return filelists


def make_imaginary_files():
    os.chdir('D:\\Music\\Новое')
    music = os.listdir()
    music = music[0:20]
    filelists = []
    n = random.randint(5,15)
    end = len(music)
    for i in range(n):
        filelists.append([])
        songs = random.randint(10,18)
        for j in range(songs):
            song = music[random.randint(0,end-1)]
            filelists[i].append(song)
    return filelists
#filelists = make_filelists()        
filelists = make_imaginary_files()
result = {}
for filelist in filelists:
    for song in filelist:
        if song not in result:
            result[song] =  1
        else:
            result[song] +=  1
list_d = list(result.items())
list_d.sort(key=lambda i: i[1])
list_d.reverse()   
print(list_d)
