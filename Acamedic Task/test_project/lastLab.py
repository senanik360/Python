import re
import json


fileName = 'E:\\Python\\Acamedic Task\\test_project\\lab.txt'
with open(fileName) as file:
    contents = file.read()
    # print(contents.strip())

FileContent={}
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

FileContent=contents
length = len(FileContent)

vowel =0
consonent =0
word = 0
digit =0
specialD=0

def checkConditions():
     for i in FileContent:
        if(i=='A' or i=='a' or i=='E' or i =='e' or i=='I'or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            vowel+=1
        elif(i==' ' or i.isdigit() or regex.search(i) != None):
                if(regex.search(i) != None):
                    word=word
                    specialD+=1
                elif(i.isdigit()):
                    digit+=1
                    
        else:
            consonent+=1
            word+=1

FileContent={
      'Content' : contents,
      'length' : length,
       'word': word,
       'vowel':vowel,
       'consonent' : consonent,
        'digit':digit,
        'Special Ch':specialD,
      }
# print(FileContent)


fileName2 = 'FileContent.json'
with open(fileName2,'w') as f:
     json.dump(FileContent,f)

with open(fileName2) as f:
    FileContent=json.load(f)

print(FileContent)
