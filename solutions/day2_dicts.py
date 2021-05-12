# Given the following dictionary:
d = {
  'times': 100,
  'name': 'George',
  'hobbies': ['fishing', 'hiking'],
}
# add key 'friends' to d with ['Andrei', 'Mihai', 'Alina'] as value
names = ['Andrei', 'Mihai', 'Alina']
d['friends'] = names
print('Dictionary after adding "friends":', d)

# sort value for key 'friends'
d['friends'].sort()
# It's the same with calling: names.sort() because `d['friends'] is names`
# assert verifies a conditions and raises AssertionError if condition is False
assert d['friends'] is names

print('Dictionary after sorting "friends":', d)
print('Names list is also sorted:', names)

# remove 'hiking' from hobbies list
d['hobbies'].remove('hiking')
print('Dictionary after removing hobby:', d)

# remove 'times' key from d
del d['times']
print('Dictionary after removing "times" key:', d)


# Given a list of strings build a dictionary that has each unique string as a
# key and the number of appearances as a value
words = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
# Version 1
occurrences = {}
for word in set(words):
    occurrences[word] = words.count(word)
print(occurrences)

# Version 1.5 (dict comprehension)
print({word: words.count(word) for word in set(words)})

# Version 2
occurrences = {}
for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1
print(occurrences)

# Version 3
occurrences = {}
for word in words:
    occurrences[word] = occurrences.get(word, 0) + 1
print(occurrences)
