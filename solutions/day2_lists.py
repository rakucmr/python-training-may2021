# Given the following list:
l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]

# Add [5, 7, 8] to the end of the list
l.extend([5, 7, 8])
print('Extended l:', l)
# l += [5, 7, 8]
# l[len(l):] = [5, 7, 8]
# print(l)

# Print the length of the list
print('List length:',  len(l))

# Check if 8 is in the list
print('8 in l:', 8 in l)

# Print the first position of 7 in the list
print('First position of 7 in l:', l.index(7))

# Count how many times 8 is in the list
print('Occurrences of 8 in l:', l.count(8))

# Reverse the list
l.reverse()  # The list is reversed in place, the function returns None
# l = l[::-1]
print('Reversed list:', l)

# Sort the list
l.sort()  # The list is sorted in place, the function returns None
print('Sorted list:', l)

# Remove all items on positions divisible by 3
del l[::3]
print('List with items on positions divisible by 3 removed:', l)


# Write a Python program to convert a list of characters into a string.
# First solution - build the string step by step
characters = ['a', 'b', 'c', 'd']
s = ''
for char in characters:
    s += char
print('First solution:', s)

# Second solution - more Pythonic, uses str.join
characters = ['a', 'b', 'c', 'd']
s = ''.join(characters)
print('Second solution:', s)


# Write a Python program to find the second smallest number in a list.
numbers = [1, 1, 3, 5, 7, 3, 8, 1, 3]

# Version 1
sorted_unique_numbers = sorted(set(numbers))
print(sorted_unique_numbers[1])

# Version 2
numbers.sort(reverse=True)
min_number = numbers[-1]
print(numbers[numbers.index(min_number) - 1])

# Version 3
min_number = second_min_number = float('inf')
for number in numbers:
    if number < min_number:
        second_min_number = min_number
        min_number = number
    elif min_number < number < second_min_number:
        second_min_number = number
print(second_min_number)
