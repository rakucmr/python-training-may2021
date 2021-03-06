"""
Initial Python script. Experiments with basic notions.
"""

# Implicit line joining
print('Hello world!',
      'Hi!',
      'Bye!')
print('This is another statement')

# Explicit line joining
x = 100 + 200 + 300 + \
    400 + 500
print(x)

# x = 0
if x:
    print('Division\'s result:', 100 / x)

multiline_str = """
sldf
aergvf
esvdf
wafsd
"""
print(multiline_str)


grade = 7
if grade > 5:
    passed = True
else:
    passed = False

passed = True if grade > 5 else False  # ternary operator

passed = grade > 5