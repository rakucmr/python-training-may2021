class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException('insufficient funds')
        self.balance -= amount


class CreditBankAccount(BankAccount):
    def __init__(self, bank_name, balance, overdraft):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise InsufficientFundsException('overdraft exceeded')
        self.balance -= amount


class Employee:
    ACCEPTED_RAISE_VALUES = (5, 10, 20)

    def __init__(self, name: str, bank_account: BankAccount, salary: int = 0):
        self.name = name
        self.bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent):
        if percent not in self.ACCEPTED_RAISE_VALUES:
            raise ValueError(f'Invalid raise value: {percent}%')
        self._salary += (percent / 100) * self._salary

    def receive_salary(self):
        self.bank_account.deposit(self._salary)


if __name__ == '__main__':
    bank_acc = BankAccount('BRD', 100)  # create instance
    print('Initial balance:', bank_acc.balance)
    bank_acc.deposit(50)  # call deposit() method
    print('Balance after depositing 50:', bank_acc.balance)  # should be 150
    bank_acc.withdraw(70)  # call withdraw() method
    print('Balance after withdrawing 70:', bank_acc.balance)  # should be 80
    try:
        bank_acc.withdraw(100)  # should raise exception
    except InsufficientFundsException as ex:
        print(ex)
    print('Balance after trying to withdraw 100:', bank_acc.balance)

    emp = Employee("John Doe", bank_acc, 1000)
    emp.raise_salary(10)
    print(emp.salary)  # should print 1100
    emp.receive_salary()
    print(emp.bank_account.balance)  # should print 1180 (80 before salary + salary)
    try:
        emp.salary = 2000  # should raise exception (can't set attribute)
    except AttributeError as ex:
        print(ex)

    credit_bank_acc = CreditBankAccount('BRD', 100, 50)  # create instance
    print('Initial balance:', credit_bank_acc.balance)
    credit_bank_acc.deposit(50)  # call deposit() method
    print('Balance after depositing 50:', credit_bank_acc.balance)  # should be 150
    credit_bank_acc.withdraw(170)  # call withdraw() method
    print('Balance after withdrawing 170:', credit_bank_acc.balance)  # should be -20
    try:
        credit_bank_acc.withdraw(100)  # should raise exception
    except InsufficientFundsException as ex:
        print(ex)
    print('Balance after trying to withdraw 100:', credit_bank_acc.balance)

    employee = Employee("Jane Doe", credit_bank_acc, 1200)
    employee.receive_salary()
    print('Balance after receiving salary (1200):', credit_bank_acc.balance)
