import unittest
from unittest.mock import patch
import employee

class TestEmployee(unittest.TestCase):
        
        # Will be executed at the beginning of all the tests once
        @classmethod
        def setUpClass(cls):
            print('setupClass')

        # Will be executed at the end of all the tests once
        @classmethod
        def tearDownClass(cls):
            print('teardownClass')


        # Will be executed before each test
        def setUp(self):
            self.emp_1 = employee.Employee('Corey', 'Schafer', 50000)
            self.emp_2 = employee.Employee('Sue', 'Smith', 60000)
        
        # Will be executed after each test
        def tearDown(self):
            pass
    
        def test_email(self):
            
    
            self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
            self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

            self.emp_1.first = 'John'
            self.emp_2.first = 'Jane'

            self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
            self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

        def test_fullname(self):
            self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
            self.assertEqual(self.emp_2.fullname, 'Sue Smith')

            self.emp_1.first = 'John'
            self.emp_2.first = 'Jane'

            self.assertEqual(self.emp_1.fullname, 'John Schafer')
            self.assertEqual(self.emp_2.fullname, 'Jane Smith')

        def test_apply_raise(self):

            self.emp_1.apply_raise()
            self.emp_2.apply_raise()

            self.assertEqual(self.emp_1.pay, 52000)
            self.assertEqual(self.emp_2.pay, 62400)

        # The patch decorator is used to mock the requests.get method
        def test_monthly_schedule(self):
            # We use the patch decorator as a context manager
            # to mock the requests.get method
            # Here the requests.get method in the employee module is mocked 
            # and the one in patch is used instead 
            with patch('employee.requests.get') as mocked_get:
                mocked_get.return_value.ok = True
                mocked_get.return_value.text = 'Success'

                schedule = self.emp_1.monthly_schedule('May')
                mocked_get.assert_called_with('http://company.com/Schafer/May')
                self.assertEqual(schedule, 'Success')

                mocked_get.return_value.ok = False

                schedule = self.emp_2.monthly_schedule('June')
                mocked_get.assert_called_with('http://company.com/Smith/June')
                self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()


           
            