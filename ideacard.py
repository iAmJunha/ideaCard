## 손정의 아이디어 카드 --ver Git
import random
import pickle

#For using in long term, should make text file
#materials = [ 'phone','laptop','watch','fruits','resumee','portpolio','drawing','clothes']

mts=[]
nword = input('put new words OR press b to break!: ')
while nword != 'b':
    materials.append(nword)
    nword = input('put new words OR press b to break! :')
    
with open('ideas.txt','w') as idea:
    for m in materials:
        idea.writelines(m+'\n')

with open('ideas.txt','r') as read:
    text=None
    while text != '':
        text=read.readline()
        print(text,type(text),end='')
    
    

'''
nword = input('put new words OR press b to break')
while nword != 'b':
    materials.append(nword)
    nword = input('put new words OR press b to break! :')

l = len(materials)

ran1 = random.randint(1,l)
ran2 = random.randint(1,l)
ran3 = random.randint(1,l)

print(materials[ran1-1],materials[ran2-1],materials[ran3-1])
'''
