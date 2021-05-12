# Given the following set:
s = set()
# Add elements from [1, 2, 3] to the set
l = [1, 2, 3]
# for elem in l:
#     s.add(elem)
# s |= set(l)
s.update(l)
print('Updated set:', s)

# Print the length of the set
print('Set length:', len(s))

# Check if 4 is in the set
print('4 in set:', 4 in s)

# Remove and print an arbitrary element from the set
print('Arbitrary element:', s.pop())
print('Set after one arbitrary element:', s)

# Remove all remaining items in the set
s.clear()
print('Set after removing all elements:', s)


# Write a Python program that counts the number of distinct words from a string.
# A word=a sequence of characters that is not whitespace (space, newline, tab).
my_str = """beautiful is better than ugly
explicit is better than implicit
simple is better than complex
complex is better than complicated
flat is better than nested
sparse is better than dense"""

print('Distinct words in string:', len(set(my_str.split())))
