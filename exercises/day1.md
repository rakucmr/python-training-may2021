### Numeric types exercises

1. Given an integer number, print its last digit. 
1. Given a three-digit number. Find the sum of its digits.
1. Given the integer `N` - the number of minutes that is passed since midnight -
 how many hours and minutes are displayed on the 24h digital clock? 
 The program should print two numbers: the number of hours (between 0 and 23) 
 and the number of minutes (between 0 and 59). 
 For example, if `N = 150`, then 150 minutes have passed since midnight - 
 i.e. now it's 2:30 am. So the program should print **2 30**.
 
 
### String exercises

1. Given the string `s = "bandana"`:
    * check if string `"and"` is contained in `s`
    * find the index of the following strings: `"n"`, `"q"`
    * how many times does the string `"an"` appear in `s`?
    * check if `s` is alphanumeric
    * transform `s` to all uppercase
    * check other methods that string supports and try them out

1. Given the string `"abcdefghijklmn"` print the following:
    * the third character of this string.
    * the second to last character of this string.
    * the first five characters of this string.
    * all but the last two characters of this string.
    * all the characters of this string with even indices (remember indexing 
    starts at 0, so the characters are displayed starting with the first).
    * all the characters of this string with odd indices 
    (i.e. starting with the second character in the string).
    * all the characters of the string in reverse order.
    * every second character of the string in reverse order, starting from the 
    last one.
    
  
### Control structures exercises

1. Write a Python program for checking the speed of drivers. 
    * If speed is less than or equal to 50, it should print `"OK"`.
    * Otherwise, for every 5 km above the speed limit (50), it should give the 
    driver one demerit point and print the total number of demerit points. 
    For example, if the speed is 60, it should print: `"Points: 2"`.
    * If the driver gets more than 12 points, it should print: 
    `"License suspended"`
 Define a variable called `speed` and assign an integer value to it. 
 After running the program once, change its value and notice the changed output.
 
1. Write a Python program which iterates the integers from 1 to 50. 
 For multiples of three print `"Fizz"` instead of the number and for the 
 multiples of five print `"Buzz"`. For numbers which are multiples of both three
 and five print `"FizzBuzz"`. If the number 30 is encountered, break the loop.
