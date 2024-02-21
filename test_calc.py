import unittest
import calc

# Create a class that inherits from unittest.TestCase
# This class will contain all the test cases
class TestCalc(unittest.TestCase):

    # Create a method that will contain the test case
    # The method name must start with test_
    def test_add(self):
        result = calc.add(10, 5)
        # Use the assertEqual method
        # to check if the result is equal to the expected value
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Use the assertRaises method to check if the function raises an exception
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # Using context manager
        with self.assertRaises(ValueError):
            calc.divide(20, 0)

    # Here 4 tests are created in total to test the add, subtract, multiply and divide functions.
    # Expected Output: Ran 4 tests in 0.001s


# The if __name__ == '__main__': construct is a common idiom used
# in Python scripts to execute some code only when the script is run directly
# and not when it's imported as a module into another script.

if __name__ == '__main__':
    # Use the main method to run the test
    unittest.main()


# To run the test, when  use the following command:
# python test_calc.py
# or
# python -m unittest test_calc.py
"""
python: This is the command used to invoke the Python interpreter.
It tells your operating system to run the Python program.

-m: This option stands for "module".
It tells the Python interpreter to run a specified module as the main program. 
When using "-m", you provide the name of the module you want to run.

unittest: This is the module name. 
Python's standard library includes a module named unittest, 
which provides a framework for writing and running tests.

test_calc.py: This is the argument passed to the "-m" option. 
It specifies the name of the Python module that contains the unit tests you want to run.
"""