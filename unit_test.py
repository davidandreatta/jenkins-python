"""
Unit test file
"""

import unittest

def isNotNull(number):
    """
    isNotNull
    """
    return bool(number)

def isEven(number):
    """
    isNotNull
    """
    if number % 2 == 0:
        return True
    return False


class TestCase(unittest.TestCase):
    """
    test class
    """
    def test_isNotNull(self):
        """
        test isNotNull
        """
        self.assertTrue(isNotNull(10))
    def test_isEven(self):
        """
        test isEven
        """
        self.assertTrue(isEven(10))


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test'))
