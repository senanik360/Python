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