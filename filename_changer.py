import os
from os import path
import shutil

#if you have a backup folder, with files that you'll not use anymore, this erase all files in the folder
for filename in os.listdir('Your directory here'):
    if os.path.isfile(os.path.join('Your directory here', filename)):
        os.remove(os.path.join('Your directory here', filename))

#select the source and the destiny folder
src = r'origin_folder'
dts = r'destiny_folder\\'

#list comprehension to move the files from the source to the destiny folder.
files = [i for i in os.listdir(src) if i.startswith("first_letter_of_file") and i.endswith("extension_of_file") and 
         path.isfile(path.join(src, i))]
for f in files:
    shutil.move(path.join(src,f),dts)

#putting all the files in the destiny folder on a list
lista=[]
for file in os.listdir(dts):
    if file.startswith('first_letter_of_file') and file.endswith('extension_of_file'):
        lista.append(file)
 
#creating another list, with the names changed, based on how much characters you want to change (in this case, the last 10)
lista2=[]
for i in lista:
    lista2.append(i[:-10]+'extension_of_file')
 
#changing the name of the first list based on the second
for i,i2 in zip(lista,lista2):
    os.rename(dts[:-1]+i,dts[:-1]+i2)