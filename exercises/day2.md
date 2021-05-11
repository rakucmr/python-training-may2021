### `try` statement exercises
1. Write a program to read two numbers: `x` and `y` from standard input and print the result of `x / y`. 
If the user inputs invalid data, display an error message and exit gracefully. 

### Lists exercises
1. Given the following list:
    ```python
    l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]
    ```
    * Add `[5, 7, 8]` to the end of the list
    * Print the length of the list
    * Check if `8` is in the list
    * Print the first position of `7` in the list
    * Count how many times `8` is in the list
    * Reverse the list
    * Sort the list
    * Remove all items on positions divisible by 3
1. Write a Python program to convert a list of characters into a string.
1. Write a Python program to find the second smallest number in a list.

### Sets exercises
1. Given the following set:
    ```python
    s = set()
    ```
    * Add elements from `[1, 2, 3]` to the set
    * Print the length of the set
    * Check if `4` is in the set
    * Remove and print an arbitrary element from the set
    * Remove all remaining items in the set
1. Write a Python program that counts the number of distinct words from a string.
A word=a sequence of characters that is not whitespace (space, newline, tab).
    
    E.g. 
    ```python
    my_str = """beautiful is better than ugly
    explicit is better than implicit
    simple is better than complex
    complex is better than complicated
    flat is better than nested
    sparse is better than dense"""
    # Should print: 14 distinct words
    ```

### Dicts exercises
1. Given the following dictionary:
    ```python
    d = {
      'times': 100, 
      'name': 'George', 
      'hobbies': ['fishing', 'hiking'],
    }
    ```
    * add key `'friends'` to `d` with `['Andrei', 'Mihai', 'Alina']` as value
    * sort value for key `'friends'`
    * remove `'hiking'` from hobbies list
    * remove `'times'` key from `d`
1. Given a list of strings build a dictionary that has each unique string as a key and the 
number of appearances as a value.
    
     E.g. `['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']` ->
`{'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}`

### Functions exercises
1. Write a function that takes a number as a parameter and prints its square.
1. Write another function that takes a number as a parameter and returns the square. 
Are the results of the two functions different? 
1. Write a function that takes any number of strings and an integer `n` as parameters.
`n` should be an optional parameter. Return the list of strings longer than `n`. 
By default, it should return a list containing all words.

    E.g. 
    * `f('hello', 'hi', 'bye', n=2)` -> `['hello', 'bye']`
    * `f('hello', 'hi')` -> `['hello', 'hi']`
    * `f()` -> `[]`
    * `f(n=10)` -> `[]`
1. [optional] Write a function that builds html tags. Apply html escaping for html special chars. 
The function will receive 2 parameters – tag type and tag content and will return the generated html as a string. 
    
    E.g.: `f('b', 'Ham&Eggs')` returns `"<b>Ham&amp;Eggs</b>"`
    
    HTML char escaping:
    * `<` becomes `&lt`;
    * `>` becomes `&gt`;
    * `"` becomes `&quot`;
    * `&` becomes `&amp`;
