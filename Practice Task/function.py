def ft():
    print("hello world!")
ft()


def fft(para):
    print(f"Hello {para}")

fft('World')


def describe_pet(animalType, petNane):
    print(f"I have a {animalType.title()}")
    print(f"{animalType.title()}'s name is {petNane.title()}")

describe_pet(animalType="hamster", petNane='harry')