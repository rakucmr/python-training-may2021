### OOP exercises
1. Create a `BankAccount` class that receives two parameters on initialisation: 
    * `bank name (str)`
    * `balance (int)`
1. Create two methods in this class, one to withdraw money and another one to deposit money into the account. The withdraw method will not allow withdrawing more money than available and it will raise an exception when you attempt to do that.
1. Create a class `Employee` with three instance attributes:
    * `person name (str)`
    * `bank account (BankAccount)`
    * `salary (default 0) (int)`

    1. Use a `property` for salary management. Salary should be set only on initialisation; you shouldn't be able to set the salary from outside the class.
    1. Write a method `raise_salary` that receives a parameter `percent` that should be one of the following values: 5, 10, 20. Raise a `ValueError` if another value is received by this method.
    The `raise_salary` method should raise the salary with 5%, 10% or 20%.
    1. Create a method `receive_salary` that will deposit in the employee's bank account an amount equal to its salary.

1. Create a `CreditBankAccount` class inherits `BankAccount` and receives one extra argument at initialisation which allows for the balance to go below zero (but not under `-overdraft`): 
    * `overdraft (int)`

    1. Override parent `withdraw` method so that the new rule is implemented.
1. Place the two bank account classes in a Python module and the employee class in another Python module. Create a third module that uses the first two modules.

#### Magic methods exercises [optional]

1. Create class `Dish` - instance attributes: `id (int)`, `name (str)`, `price (int)`
1. Create class `Menu` - instance attributes: `dishes (list of Dish objects)`.

    Implement appropriate methods so that `Menu` objects support the following operations:
    ```python
    d = Dish(0, 'Lasagna', 20)
    m = Menu()
    m += d  # dish appended to m.dishes
    m[0]  # implement getitem on Menu
    d in m  # implement membership test operators
    len(m)  # return length of m.dishes
    ```
### Files exercises

1. Write a Python program that reads file content and displays the number of lines that were read.
1. Write a Python program to append text into a file and display the new content.
1. Write a function `grep` that receives `text` and `file` as parameters and returns a list with all the lines in the file containing `text`. 
1. Write another function `grepinto` that receives `text`, `infile` and `outfile` as parameters and writes to `outfile` the lines in `infile` that contain `text`. Open both files within one `with` statement. 

[!] `file`, `infile` and `outfile` are all file names - not file handlers.

### File system exercises

1. Write a Python program that creates a directory `outdir` at the current location and a directory `innerdir` inside `outdir`.
   Create an empty file inside `innerdir`. Use `os.walk()` to print the directory tree for `outdir`.
   Remove the directories and the file.
1. Write a generator function that yields all the file names with an extension from a directory.
   Give the path and the file extension as parameters. 
