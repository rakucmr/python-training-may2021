# str and int are type hints; they suggest the types for the parameters &
# return value
def f(name: str, age: int) -> str:
    """
    Prints a message about a person
    :param name: str
    :param age: int
    :return: str
    """
    return f'{name} is {age} years old.'


message = f('Ana', 20)
print(message)
