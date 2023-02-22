class MyClass:
    x = 5

obj = MyClass()


print(obj.x)



class Demo:

    def __init__(self):
       print('hello')

obj = Demo()

class pick:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dept= 0 # default value

    def cls(self, name, age):
        self.name = name
        self.age = age
        print("hello from pick")
            

obj = pick('anik', 23)
obt = pick('alok', 20)

print(obj.name)
print(obt.name)
print(obt.dept)

class pickN(pick):
        def __init__(self, name, age):
            self.name = name
            self.age = age
            print(name)
            print(age)

       
obj = pickN('anushree', 4)
obj.cls('anik', 23)
