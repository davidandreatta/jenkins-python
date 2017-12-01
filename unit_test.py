import unittest

def isNotNull(number):
    if number != 0:
        return True
    else:
        return False

class TestCase(unittest.TestCase):
    def test_isNotNull(self):
        self.assertTrue(isNotNull(10))

if __name__ == '__main__':
    unittest.main()
