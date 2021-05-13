from datetime import date, timedelta


class Person:
    count = 0  # class attribute

    def __init__(self, name, date_of_birth):
        self.name = name   # instance attribute
        self.increment_count()
        self.date_of_birth = date_of_birth

    def salute(self, greeting):  # instance method
        print(f'{self.name} says "{greeting}!"')

    def _get_age(self):
        diff = date.today() - self._date_of_birth
        return int(diff.days / 365.25)

    @property  # using property for computed attributes
    def age(self):
        return self._get_age()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        if date.today() - timedelta(weeks=6000) > value:
            raise ValueError('You cannot be that old')
        self._date_of_birth = value

    @classmethod
    def increment_count(cls):  # class method
        cls.count += 1

    def __str__(self):
        return f'Person (name={self.name})'

    def __repr__(self):
        return f'Person object {self.__dict__}'

    def __eq__(self, other):
        return self.name == other.name


if __name__ == '__main__':
    print(Person.count)
    p = Person('Ana', date(1999, 2, 4))
    print(Person.count)
    p2 = Person('Mihai', date(1984, 12, 23))
    print(p.name)
    print(p2.name)

    p.name = 'Dana'
    print(p.name)

    print(Person.count)

    p.salute('Hello')
    p2.salute('Good morning')

    Person.increment_count()
    p.increment_count()
    print(Person.count)

    # using protected attributes outside the class is not recommended
    # print(f"{p.name}'s age:", p._get_age())

    print(f"{p.name}'s age:", p.age)

    print(p.date_of_birth)
    p.date_of_birth = date(1990, 3, 5)
    print(f"{p.name}'s age:", p.age)
