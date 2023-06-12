import unittest
from unittest.mock import patch
from Employee import *


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """"Run only once at the beginning of the tests run"""
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """"Run only once at the end of all tests run"""
        print('teardownClass')

    def setUp(self):
        """Run the code before every test one by one"""
        print('setup')
        self.emp_1 = Employee('Amit', 'Chen', 50000)
        self.emp_2 = Employee('Yoav', 'Barbi', 60000)

    def tearDown(self):
        """"Run the code after every test one by one"""
        print('tearDown')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Amit.Chen@email.com')
        self.assertEqual(self.emp_2.email, 'Yoav.Barbi@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Amit Chen')
        self.assertEqual(self.emp_2.fullname, 'Yoav Barbi')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Chen')
        self.assertEqual(self.emp_2.fullname, 'Jane Barbi')

    def test_apply_raise(self):
        print('apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """"Checking case of Website URL get OK response
        and case of Bad response using mock"""
        with patch('Employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Chen/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Barbi/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
