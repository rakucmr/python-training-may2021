import unittest

from solutions.day4_oop import Employee


class EmployeeRaiseSalaryTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Test", None, 100)

    def test_invalid_raise_value(self):
        with self.assertRaises(ValueError):
            self.employee.raise_salary(50)

    def test_salary_equal_to_zero(self):
        employee = Employee("Test", None)
        employee.raise_salary(5)
        self.assertEqual(employee.salary, 0)

    def test_raise_salary_success(self):
        for raise_value in Employee.ACCEPTED_RAISE_VALUES:
            with self.subTest(f'Error for raise_value={raise_value}'):
                before_raise = self.employee.salary
                self.employee.raise_salary(raise_value)
                self.assertEqual(
                    self.employee.salary,
                    before_raise + before_raise * raise_value / 100
                )
