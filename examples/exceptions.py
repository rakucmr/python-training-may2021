greeting = input('What is your greeting? ')
try:
    print(greeting[5])
except IndexError as ex:
    print('exception occurred:', ex.__class__.__name__)
