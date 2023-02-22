def ft():
    print("hello world!")


ft()


def fft(para):
    print(f"Hello {para}")


fft('World')


def describe_pet(animalType, petNane):  #
    print(f"I have a {animalType.title()}")
    print(f"{animalType.title()}'s name is {petNane.title()}")


describe_pet("hamster", 'harry')  # positional Arguments
'''
When you call a function, Python must match each argument in the
function call with a parameter in the function definition. The simplest way
to do this is based on the order of the arguments provided. Values
matched up this way are called positional arguments.'''
describe_pet(petNane='harry', animalType="hamster")  # Keyword Arguments
'''
• A keyword argument is a name-value pair that you pass to a function.
Keyword arguments free you from having to worry about correctly ordering your
arguments in the function call, and they clarify the role of each value in the
function call.
'''


def pokpok(name, id=56):
    print(f"name is {name.title()}")
    print(f"id is {id}")


pokpok('tok')
'''
When you use default values, any parameter with a default value needs to
be listed after all the parameters that don’t have default values. This allows
Python to continue interpreting positional arguments correctly.'''


def pokpok(name, id=""):
    print(f"name is {name.title()}")
    print(f"id is {id}")


pokpok('mok')
pokpok('mok', 67)
'''
sometimes it makes sense to make an argument optional so that people using
the function can choose to provide extra information only if they want to. You can
use default values to make an argument optional.'''


def usersF(users):
    for i in users:
        print(i.title(), end=' ')


users=['anik', 'alok', 'anushree']

usersF(users) #passing a list
'''
When you pass a list to a function, the function gets direct access to
the contents of the list.'''



def nakani(*jaIccha): # an Arbitrary Number of parameter
    print(jaIccha)

nakani('hello','valo','ok') #Passing an Arbitrary Number of Arguments

'''The asterisk (*) in the parameter name *toppings tells Python to make an empty
tuple called toppings and pack whatever values it receives into this tuple.'''

def nakani2(name,*jaIccha): # aMixing Positional and Arbitrary Parameters
    print(name)
    print(jaIccha)

nakani2('anik','valo','ok') #Mixing Positional and Arbitrary Arguments

'''If you want a function to accept several different kinds of arguments, the parameter that
accepts an arbitrary number of arguments must be placed last in the function definition.
Python matches positional and keyword arguments first and then collects any remaining
arguments in the final parameter.
• You will often see the generic parameter name *args, which collects arbitrary positional
arguments.'''


def demo(*args):
    print(args)

demo('hello', 'tello', 'mello')
'''*args allows you to pass the desired number of arguments to the function. '''

def demo2(**kwargs):
    print(kwargs)

demo2(hello='Hello', tello='Tello')

'''**kwargs stands for keyword arguments. The only difference from args is that it uses keywords and returns the values in the form of a dictionary. '''