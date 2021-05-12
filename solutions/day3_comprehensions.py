import string

# Create a dict {"a": 97, "b": 98, ... } using comprehension. Use ord built-in
# to obtain ASCII code. Keys range from "a" to "e".
d1 = {letter: ord(letter) for letter in string.ascii_letters if letter <= 'e'}

# Using the dictionary generated above, create another one where you swap keys and values.
d2 = {ascii_code: letter for letter, ascii_code in d1.items()}
# d2 = {d1[letter]: letter for letter in d1.keys()}  # version above is more explicit

# Filter the above dictionary to contain only even keys.
d3 = {ascii_code: letter for ascii_code, letter in d2.items() if ascii_code % 2 == 0}

# Can you obtain dictionary from ex. 3 from the given string ("abcde") in a single dict comprehension?
d4 = {ord(letter): letter for letter in string.ascii_letters[:5] if ord(letter) % 2 == 0}


print(d1)
print(d2)
print(d3)
print(d4)
