import unittest

def isNotNull(number):
    if number != 0:
        return True
    else:
        return False
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


class TestCase(unittest.TestCase):
    def test_isNotNull(self):
        self.assertTrue(isNotNull(10))
    def test_isEven(self):
        self.assertTrue(isEven(10))


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test'))
