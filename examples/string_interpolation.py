name = 'Tom'
age = 5

print(name + ' is ' + str(age) + ' years old')
print(name, 'is', age, 'years old')
print('%s is %d years old. %s is a good cat.' % (name, age, name))
print('{} is {} years old.'.format(name, age))
print('{0} is {1} years old. {0} is a good cat.'.format(name, age))
print('{nm} is {ag} years old. {nm} is a good cat.'.format(nm=name, ag=age))

print(f'{name} is {age} years old. {name.upper()} is a good cat. In 10 years he'
      f' will be {age + 10}.')

print(f'{print} is a function')
