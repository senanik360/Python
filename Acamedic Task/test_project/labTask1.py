import re
user={}
u_input=input('Write a line : ')
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

user['string']=u_input
length = len(user['string'])

vowel =0
consonent =0
word = 0
digit =0
specialD=0

for i in user['string']:
    if(i=='A' or i=='a' or i=='E' or i =='e' or i=='I'or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
        vowel+=1
    else:
        consonent+=1
    if(i==' ' or i.isdigit()):
            if(regex.search(i) == None):
                word=word
                digit+=1
            else:
                specialD+=1 
                
    else:
            word+=1

user['string']={
      u_input :{
      'info' : {
      'length' : length,
       'word': word,
       'vowel':vowel,
        'consonent' : consonent,
        'digit':digit,
        'Special Ch':specialD,
      }
      }
}
print(user)

