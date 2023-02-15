name = ['anik', 'alok', 'anushree']




num = [1,2,3,4,5,6,7,8,9,10]

print(min(num))
print(max(num))
print(sum(num))

sq = [value**2 for value in range(1,11)]

print(sq)
players = ['a','b','a','b','a','b']

player=players[:]

print(player)
player[0]='c'
print(player)
print(players)



cars={'ab':'ba', 'bc':'cb'}

for key,value in cars.items():
    print(key+"  :  "+value)


for i in set(players):
    print(i.title())

check = ['and', 'or', 'not']

print(check[0])

fname = 'anik'
lname = 'sen'

print("{} {}".format(fname,lname))

